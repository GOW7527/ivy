# global
from typing import Union, Optional

import torch

# local
import ivy
from ivy.func_wrapper import with_unsupported_dtypes, handle_numpy_array_in_torch
from ivy import promote_types_of_inputs
from . import backend_version


def _cast_for_unary_op(x):
    if not isinstance(x, torch.Tensor):
        x = torch.tensor(x)
    return x


@handle_numpy_array_in_torch
def add(
    x1: Union[float, torch.Tensor],
    x2: Union[float, torch.Tensor],
    /,
    *,
    alpha: Optional[Union[int, float]] = None,
    out: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    x1, x2 = ivy.promote_types_of_inputs(x1, x2)
    if alpha not in (1, None):
        return torch.add(x1, x2, alpha=alpha, out=out)
    return torch.add(x1, x2, out=out)


add.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torch
def bitwise_xor(
    x1: Union[int, bool, torch.Tensor],
    x2: Union[int, bool, torch.Tensor],
    /,
    *,
    out: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    x1, x2 = ivy.promote_types_of_inputs(x1, x2, array_api_promotion=True)
    return torch.bitwise_xor(x1, x2, out=out)


bitwise_xor.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torchdef expm1(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.expm1(x, out=out)


expm1.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torchdef bitwise_invert(
    x: Union[int, bool, torch.Tensor], /, *, out: Optional[torch.Tensor] = None
) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.bitwise_not(x, out=out)


bitwise_invert.support_native_out = True


@handle_numpy_array_in_torch
def isfinite(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.isfinite(x)


@handle_numpy_array_in_torch
def isinf(
    x: torch.Tensor,
    /,
    *,
    detect_positive: bool = True,
    detect_negative: bool = True,
    out: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    if detect_negative and detect_positive:
        return torch.isinf(x)
    elif detect_negative:
        return torch.isneginf(x)
    elif detect_positive:
        return torch.isposinf(x)
    return torch.full_like(x, False, dtype=torch.bool)


@handle_numpy_array_in_torch
def equal(
    x1: Union[float, torch.Tensor],
    x2: Union[float, torch.Tensor],
    /,
    *,
    out: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    x1, x2 = ivy.promote_types_of_inputs(x1, x2)
    return torch.eq(x1, x2, out=out)


equal.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torchdef less_equal(
    x1: Union[float, torch.Tensor],
    x2: Union[float, torch.Tensor],
    /,
    *,
    out: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    x1, x2 = ivy.promote_types_of_inputs(x1, x2)
    return torch.less_equal(x1, x2, out=out)


less_equal.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torchdef bitwise_and(
    x1: Union[int, bool, torch.Tensor],
    x2: Union[int, bool, torch.Tensor],
    /,
    *,
    out: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    x1, x2 = ivy.promote_types_of_inputs(x1, x2, array_api_promotion=True)
    return torch.bitwise_and(x1, x2, out=out)


bitwise_and.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torchdef ceil(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    if "int" in str(x.dtype):
        if ivy.exists(out):
            return ivy.inplace_update(out, x)
        return x
    return torch.ceil(x, out=out)


ceil.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torchdef floor(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    if "int" in str(x.dtype):
        if ivy.exists(out):
            return ivy.inplace_update(out, x)
        return x
    return torch.floor(x, out=out)


floor.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torchdef asin(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.asin(x, out=out)


asin.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torchdef asinh(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.asinh(x, out=out)


asinh.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torchdef sign(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.sign(x, out=out)


sign.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torchdef sqrt(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.sqrt(x, out=out)


sqrt.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torchdef cosh(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.cosh(x, out=out)


cosh.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torchdef log10(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.log10(x, out=out)


log10.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torchdef log2(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.log2(x, out=out)


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torchdef log1p(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.log1p(x, out=out)


log1p.support_native_out = True


@handle_numpy_array_in_torch
def isnan(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.isnan(x)


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torchdef less(
    x1: Union[float, torch.Tensor],
    x2: Union[float, torch.Tensor],
    /,
    *,
    out: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    x1, x2 = ivy.promote_types_of_inputs(x1, x2)
    return torch.lt(x1, x2, out=out)


less.support_native_out = True


@handle_numpy_array_in_torch
def multiply(
    x1: Union[float, torch.Tensor],
    x2: Union[float, torch.Tensor],
    /,
    *,
    out: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    x1, x2 = ivy.promote_types_of_inputs(x1, x2)
    return torch.multiply(x1, x2, out=out)


multiply.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torchdef cos(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.cos(x, out=out)


cos.support_native_out = True


@handle_numpy_array_in_torch
def logical_not(
    x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None
) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.logical_not(x.type(torch.bool), out=out)


logical_not.support_native_out = True


@handle_numpy_array_in_torch
def divide(
    x1: Union[float, torch.Tensor],
    x2: Union[float, torch.Tensor],
    /,
    *,
    out: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    x1, x2 = ivy.promote_types_of_inputs(x1, x2)
    ret = torch.div(x1, x2)
    if ivy.is_float_dtype(x1.dtype) or ivy.is_complex_dtype(x1.dtype):
        ret = ivy.astype(ret, x1.dtype, copy=False)
    else:
        ret = ivy.astype(ret, ivy.default_float_dtype(as_native=True), copy=False)
    return ret


divide.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torchdef greater(
    x1: Union[float, torch.Tensor],
    x2: Union[float, torch.Tensor],
    /,
    *,
    out: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    x1, x2 = ivy.promote_types_of_inputs(x1, x2)
    return torch.greater(x1, x2, out=out)


greater.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torchdef greater_equal(
    x1: Union[float, torch.Tensor],
    x2: Union[float, torch.Tensor],
    /,
    *,
    out: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    x1, x2 = ivy.promote_types_of_inputs(x1, x2)
    return torch.greater_equal(x1, x2, out=out)


greater_equal.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torchdef acos(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.acos(x, out=out)


acos.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torch
def lcm(
    x1: torch.Tensor,
    x2: torch.Tensor,
    /,
    *,
    out: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    x1, x2 = promote_types_of_inputs(x1, x2)
    return torch.abs(torch.lcm(x1, x2, out=out))


lcm.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torch
def logical_xor(
    x1: torch.Tensor, x2: torch.Tensor, /, *, out: Optional[torch.Tensor] = None
) -> torch.Tensor:
    return torch.logical_xor(x1.type(torch.bool), x2.type(torch.bool), out=out)


logical_xor.support_native_out = True


@handle_numpy_array_in_torch
def logical_and(
    x1: torch.Tensor, x2: torch.Tensor, /, *, out: Optional[torch.Tensor] = None
) -> torch.Tensor:
    return torch.logical_and(x1.type(torch.bool), x2.type(torch.bool), out=out)


logical_and.support_native_out = True


@handle_numpy_array_in_torch
def logical_or(
    x1: torch.Tensor, x2: torch.Tensor, /, *, out: Optional[torch.Tensor] = None
) -> torch.Tensor:
    return torch.logical_or(x1.type(torch.bool), x2.type(torch.bool), out=out)


logical_or.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torch
def acosh(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.acosh(x, out=out)


acosh.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torch
def sin(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.sin(x, out=out)


sin.support_native_out = True


@handle_numpy_array_in_torch
def negative(
    x: Union[float, torch.Tensor], /, *, out: Optional[torch.Tensor] = None
) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.neg(x, out=out)


negative.support_native_out = True


@handle_numpy_array_in_torch
def not_equal(
    x1: Union[float, torch.Tensor],
    x2: Union[float, torch.Tensor],
    /,
    *,
    out: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    x1, x2 = ivy.promote_types_of_inputs(x1, x2)
    return torch.not_equal(x1, x2, out=out)


not_equal.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torch
def tanh(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.tanh(x, out=out)


tanh.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torch
def floor_divide(
    x1: Union[float, torch.Tensor],
    x2: Union[float, torch.Tensor],
    /,
    *,
    out: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    x1, x2 = ivy.promote_types_of_inputs(x1, x2)
    if ivy.exists(out):
        if not ivy.is_float_dtype(out):
            return ivy.inplace_update(
                out, torch.floor(torch.div(x1, x2)).type(out.dtype)
            )
    return torch.floor(torch.div(x1, x2), out=out).type(x1.dtype)


floor_divide.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torch
def bitwise_or(
    x1: Union[int, bool, torch.Tensor],
    x2: Union[int, bool, torch.Tensor],
    /,
    *,
    out: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    x1, x2 = ivy.promote_types_of_inputs(x1, x2, array_api_promotion=True)
    return torch.bitwise_or(x1, x2, out=out)


bitwise_or.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torch
def sinh(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.sinh(x, out=out)


sinh.support_native_out = True


@handle_numpy_array_in_torch
def positive(
    x: Union[float, torch.Tensor], /, *, out: Optional[torch.Tensor] = None
) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.positive(x)


@handle_numpy_array_in_torch
def square(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.square(x, out=out)


square.support_native_out = True


@handle_numpy_array_in_torch
def pow(
    x1: Union[float, torch.Tensor],
    x2: Union[float, torch.Tensor],
    /,
    *,
    out: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    x1, x2 = ivy.promote_types_of_inputs(x1, x2)
    return torch.pow(x1, x2, out=out)


pow.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torch
def round(
    x: torch.Tensor, /, *, decimals: int = 0, out: Optional[torch.Tensor] = None
) -> torch.Tensor:
    if "int" in str(x.dtype):
        if ivy.exists(out):
            return ivy.inplace_update(out, x)
        return x
    return torch.round(x, decimals=decimals, out=out)


round.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torch
def trunc(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    if "int" not in str(x.dtype):
        return torch.trunc(x, out=out)
    ret = x
    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


trunc.support_native_out = True


@handle_numpy_array_in_torch
def abs(
    x: Union[float, torch.Tensor],
    /,
    *,
    where: Union[bool, torch.Tensor] = True,
    out: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    if x.dtype is torch.bool:
        return x
    return ivy.where(where, torch.abs(x, out=out), x)


abs.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torch
def logaddexp(
    x1: torch.Tensor, x2: torch.Tensor, /, *, out: Optional[torch.Tensor] = None
) -> torch.Tensor:
    x1, x2 = ivy.promote_types_of_inputs(x1, x2)
    return torch.logaddexp(x1, x2, out=out)


logaddexp.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torch
def tan(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.tan(x, out=out)


tan.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torch
def atan(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.atan(x, out=out)


atan.support_native_out = True


@with_unsupported_dtypes(
    {"2.0.1 and below": ("float16", "bfloat16", "complex")}, backend_version
)  # TODO Fixed in PyTorch 1.12.1 (this note excludes complex)
@handle_numpy_array_in_torch
def atan2(
    x1: torch.Tensor, x2: torch.Tensor, /, *, out: Optional[torch.Tensor] = None
) -> torch.Tensor:
    x1, x2 = ivy.promote_types_of_inputs(x1, x2)
    return torch.atan2(x1, x2, out=out)


atan2.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torch
def log(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.log(x, out=out)


log.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torch
def exp(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.exp(x, out=out)


exp.support_native_out = True


@handle_numpy_array_in_torch
def subtract(
    x1: Union[float, torch.Tensor],
    x2: Union[float, torch.Tensor],
    /,
    *,
    alpha: Optional[Union[int, float]] = None,
    out: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    x1, x2 = ivy.promote_types_of_inputs(x1, x2)
    if alpha not in (1, None):
        return torch.subtract(x1, x2, alpha=alpha, out=out)
    return torch.subtract(x1, x2, out=out)


subtract.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torch
def remainder(
    x1: Union[float, torch.Tensor],
    x2: Union[float, torch.Tensor],
    /,
    *,
    modulus: bool = True,
    out: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    x1, x2 = ivy.promote_types_of_inputs(x1, x2)
    if not modulus:
        res = x1 / x2
        res_floored = torch.where(res >= 0, torch.floor(res), torch.ceil(res))
        diff = res - res_floored
        diff, x2 = ivy.promote_types_of_inputs(diff, x2)
        if ivy.exists(out):
            if out.dtype != x2.dtype:
                return ivy.inplace_update(
                    out, torch.round(torch.mul(diff, x2)).to(out.dtype)
                )
        return torch.round(torch.mul(diff, x2), out=out).to(x1.dtype)
    return torch.remainder(x1, x2, out=out).to(x1.dtype)


remainder.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torch
def atanh(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.atanh(x, out=out)


atanh.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torch
def bitwise_right_shift(
    x1: Union[int, bool, torch.Tensor],
    x2: Union[int, bool, torch.Tensor],
    /,
    *,
    out: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    x1, x2 = ivy.promote_types_of_inputs(x1, x2, array_api_promotion=True)
    x2 = torch.clamp(x2, min=0, max=torch.iinfo(x2.dtype).bits - 1)
    return torch.bitwise_right_shift(x1, x2, out=out)


bitwise_right_shift.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torch
def bitwise_left_shift(
    x1: Union[int, bool, torch.Tensor],
    x2: Union[int, bool, torch.Tensor],
    /,
    *,
    out: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    x1, x2 = ivy.promote_types_of_inputs(x1, x2, array_api_promotion=True)
    return torch.bitwise_left_shift(x1, x2, out=out)


bitwise_left_shift.support_native_out = True


# Extra #
# ------#


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torch
def erf(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.erf(x, out=out)


erf.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torch
def minimum(
    x1: Union[float, torch.Tensor],
    x2: Union[float, torch.Tensor],
    /,
    *,
    use_where: bool = True,
    out: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    x1, x2 = ivy.promote_types_of_inputs(x1, x2)
    if use_where:
        ret = torch.where(x1 <= x2, x1, x2)
        if ivy.exists(out):
            return ivy.inplace_update(out, ret)
        return ret
    return torch.minimum(x1, x2, out=out)


minimum.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torch
def maximum(
    x1: Union[float, torch.Tensor],
    x2: Union[float, torch.Tensor],
    /,
    *,
    use_where: bool = True,
    out: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    x1, x2 = ivy.promote_types_of_inputs(x1, x2)
    if use_where:
        ret = torch.where(x1 >= x2, x1, x2)
        if ivy.exists(out):
            return ivy.inplace_update(out, ret)
        return ret
    return torch.maximum(x1, x2, out=out)


maximum.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torch
def reciprocal(
    x: Union[float, torch.Tensor], /, *, out: Optional[torch.Tensor] = None
) -> torch.Tensor:
    x = _cast_for_unary_op(x)
    return torch.reciprocal(x, out=out)


reciprocal.support_native_out = True


@handle_numpy_array_in_torch
def deg2rad(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    return torch.deg2rad(x, out=out)


deg2rad.support_native_out = True


@handle_numpy_array_in_torch
def rad2deg(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    return torch.rad2deg(x, out=out)


rad2deg.support_native_out = True


@with_unsupported_dtypes({"2.0.1 and below": ("complex",)}, backend_version)
@handle_numpy_array_in_torch
def trunc_divide(
    x1: Union[float, torch.Tensor],
    x2: Union[float, torch.Tensor],
    /,
    *,
    out: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    x1, x2 = ivy.promote_types_of_inputs(x1, x2)
    ret = torch.div(x1, x2, rounding_mode="trunc")
    if ivy.is_float_dtype(x1.dtype):
        ret = ret.to(x1.dtype)
    else:
        ret = ret.to(ivy.default_float_dtype(as_native=True))
    return ret


@handle_numpy_array_in_torch
def isreal(x: torch.Tensor, /, *, out: Optional[torch.Tensor] = None) -> torch.Tensor:
    return torch.isreal(x)


@with_unsupported_dtypes(
    {"2.0.1 and below": ("bfloat16", "complex")},
    backend_version,
)
@handle_numpy_array_in_torch
def fmod(
    x1: torch.Tensor,
    x2: torch.Tensor,
    /,
    *,
    out: Optional[torch.Tensor] = None,
) -> torch.Tensor:
    x1, x2 = promote_types_of_inputs(x1, x2)
    return torch.fmod(x1, x2, out=None)


fmod.support_native_out = True
