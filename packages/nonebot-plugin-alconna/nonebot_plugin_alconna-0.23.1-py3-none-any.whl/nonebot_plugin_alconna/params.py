import inspect
from typing_extensions import Annotated, TypeAlias, get_args
from typing import (
    Any,
    Dict,
    Type,
    Tuple,
    Union,
    Literal,
    TypeVar,
    Callable,
    Optional,
    overload,
)

from nonebot.typing import T_State
from tarina import run_always_await
from nepattern.util import CUnionType
from pydantic.fields import Undefined
from tarina.generic import get_origin
from nonebot.dependencies import Param
from nonebot.internal.params import Depends
from nonebot.internal.matcher import Matcher
from nonebot.internal.adapter import Bot, Event
from arclet.alconna.builtin import generate_duplication
from arclet.alconna import Empty, Alconna, Arparma, Duplication

from .uniseg.message import TS, UniMessage
from .model import T, Match, Query, CommandResult
from .consts import ALCONNA_RESULT, ALCONNA_ARG_KEY, ALCONNA_EXEC_RESULT

T_Duplication = TypeVar("T_Duplication", bound=Duplication)
MIDDLEWARE: TypeAlias = Callable[[Bot, T_State, Any], Any]
_Contents = (Union, CUnionType, Literal)


def _alconna_result(state: T_State) -> CommandResult:
    return state[ALCONNA_RESULT]


def AlconnaResult() -> CommandResult:
    return Depends(_alconna_result, use_cache=False)


def _alconna_exec_result(state: T_State) -> Dict[str, Any]:
    return state[ALCONNA_EXEC_RESULT]


def AlconnaExecResult() -> Dict[str, Any]:
    return Depends(_alconna_exec_result, use_cache=False)


def _alconna_matches(state: T_State) -> Arparma:
    return _alconna_result(state).result


def AlconnaMatches() -> Arparma:
    return Depends(_alconna_matches, use_cache=False)


def AlconnaMatch(name: str, middleware: Optional[MIDDLEWARE] = None) -> Match:
    async def _alconna_match(state: T_State, bot: Bot) -> Match:
        arp = _alconna_result(state).result
        mat = Match(arp.all_matched_args.get(name, Empty), name in arp.all_matched_args)
        if middleware and mat.available:
            mat.result = await run_always_await(middleware, bot, state, mat.result)
        return mat

    return Depends(_alconna_match, use_cache=False)


def AlconnaQuery(
    path: str,
    default: Union[T, Empty] = Empty,
    middleware: Optional[MIDDLEWARE] = None,
) -> Query[T]:
    async def _alconna_query(state: T_State, bot: Bot) -> Query:
        arp = _alconna_result(state).result
        q = Query(path, default)
        result = arp.query(path, Empty)
        q.available = result != Empty
        if q.available:
            q.result = result  # type: ignore
        elif default != Empty:
            q.available = True
        if middleware and q.available:
            q.result = await run_always_await(middleware, bot, state, q.result)
        return q

    return Depends(_alconna_query, use_cache=False)


@overload
def AlconnaDuplication() -> Duplication:
    ...


@overload
def AlconnaDuplication(__t: Type[T_Duplication]) -> T_Duplication:
    ...


def AlconnaDuplication(__t: Optional[Type[T_Duplication]] = None) -> Duplication:
    def _alconna_match(state: T_State) -> Duplication:
        res = _alconna_result(state)
        gt = __t or generate_duplication(res.source)
        return gt(res.result)

    return Depends(_alconna_match, use_cache=False)


def AlconnaArg(path: str) -> Any:
    def _alconna_arg(state: T_State) -> Any:
        return state[ALCONNA_ARG_KEY.format(key=path)]

    return Depends(_alconna_arg, use_cache=False)


async def _uni_msg(bot: Bot, event: Event) -> UniMessage:
    return await UniMessage.generate(event, bot)


def UniversalMessage() -> UniMessage:
    return Depends(_uni_msg, use_cache=True)


def UniversalSegment(t: Type[TS], index: int = 0) -> TS:
    async def _uni_seg(bot: Bot, event: Event) -> TS:
        return (await UniMessage.generate(event, bot))[t, index]

    return Depends(_uni_seg, use_cache=True)


AlcResult = Annotated[CommandResult, AlconnaResult()]
AlcExecResult = Annotated[Dict[str, Any], AlconnaExecResult()]
AlcMatches = Annotated[Arparma, AlconnaMatches()]
UniMsg = Annotated[UniMessage, UniversalMessage()]


def match_path(path: str):
    """
    当 Arpamar 解析成功后, 依据 path 是否存在以继续执行事件处理

    当 path 为 ‘$main’ 时表示认定当且仅当主命令匹配
    """

    def wrapper(result: Arparma):
        if path == "$main":
            return not result.components
        else:
            return result.query(path, "\0") != "\0"

    return wrapper


def match_value(path: str, value: Any, or_not: bool = False):
    """
    当 Arpamar 解析成功后, 依据查询 path 得到的结果是否符合传入的值以继续执行事件处理

    当 or_not 为真时允许查询 path 失败时继续执行事件处理
    """

    def wrapper(result: Arparma):
        if result.query(path, "\0") == value:
            return True
        return or_not and result.query(path, "\0") == "\0"

    return wrapper


_seminal = type("_seminal", (object,), {})


def assign(
    path: str, value: Any = _seminal, or_not: bool = False
) -> Callable[[Arparma], bool]:
    if value != _seminal:
        return match_value(path, value, or_not)
    if or_not:
        return lambda x: match_path("$main")(x) or match_path(path)(x)  # type: ignore
    return match_path(path)


def Check(fn: Callable[[Arparma], bool]) -> bool:
    def _arparma_check(state: T_State, matcher: Matcher) -> bool:
        arp = _alconna_result(state).result
        if not (ans := fn(arp)):
            matcher.skip()
        return ans

    return Depends(_arparma_check, use_cache=False)


class AlconnaParam(Param):
    """Alconna 相关注入参数

    本注入解析事件响应器操作 `AlconnaMatcher` 的响应函数内所需参数。
    """

    def __repr__(self) -> str:
        return f"AlconnaParam(type={self.extra['type']!r})"

    @classmethod
    def _check_param(
        cls, param: inspect.Parameter, allow_types: Tuple[Type[Param], ...]
    ) -> Optional["AlconnaParam"]:
        annotation = get_origin(param.annotation)
        if annotation in _Contents:
            annotation = get_args(param.annotation)[0]
        if annotation is CommandResult:
            return cls(..., type=CommandResult)
        if annotation is Arparma:
            return cls(..., type=Arparma)
        if annotation is Alconna:
            return cls(..., type=Alconna)
        if annotation is Duplication:
            return cls(..., type=Duplication)
        if inspect.isclass(annotation) and issubclass(annotation, Duplication):
            return cls(..., anno=param.annotation, type=Duplication)
        if annotation is Match:
            return cls(param.default, name=param.name, type=Match)
        if isinstance(param.default, Query):
            return cls(param.default, type=Query)
        return cls(param.default, name=param.name, type=Any, validate=True)

    async def _solve(self, state: T_State, **kwargs: Any) -> Any:
        t = self.extra["type"]
        res = _alconna_result(state)
        if t is CommandResult:
            return res
        if t is Arparma:
            return res.result
        if t is Alconna:
            return res.source
        if t is Duplication:
            if anno := self.extra.get("anno"):
                return anno(res.result)
            else:
                return generate_duplication(res.source)(res.result)
        if t is Match:
            target = res.result.all_matched_args.get(self.extra["name"], Empty)
            return Match(target, target != Empty)
        if t is Query:
            q = Query(self.default.path, self.default.result)
            result = res.result.query(q.path, Empty)
            q.available = result != Empty
            if q.available:
                q.result = result
            elif self.default.result != Empty:
                q.available = True
            return q
        if (key := ALCONNA_ARG_KEY.format(key=self.extra["name"])) in state:
            return state[key]
        if self.extra["name"] in res.result.all_matched_args:
            return res.result.all_matched_args[self.extra["name"]]
        return self.default if self.default not in (..., Empty) else Undefined

    async def _check(self, state: T_State, **kwargs: Any) -> Any:
        if self.extra["type"] == Any:
            if (
                self.extra["name"] in _alconna_result(state).result.all_matched_args
                or ALCONNA_ARG_KEY.format(key=self.extra["name"]) in state
            ):
                return True
            if self.default not in (..., Empty):
                return True


class _Dispatch:
    def __init__(
        self,
        path: str,
        value: Any = _seminal,
        or_not: bool = False,
    ):
        self.fn = assign(path, value, or_not)
        self.result = None

    def set(self, arp: AlcResult):
        self.result = arp

    def __call__(self, _state: T_State) -> bool:
        if self.result is None:
            return False
        if self.fn(self.result.result):
            _state[ALCONNA_RESULT] = self.result
            self.result = None
            return True
        return False
