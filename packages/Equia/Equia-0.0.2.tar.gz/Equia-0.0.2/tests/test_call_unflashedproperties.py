import pytest
from equia.models import CalculationComposition, ProblemDetails 
from equia.equia_client import EquiaClient
from equia.demofluids.fluids import nHexane_Ethylene_HDPE7

@pytest.mark.asyncio
async def test_call_unflashedproperties():
    client = EquiaClient(
      "https://localhost:5201", "9DABA1C2-ACDA-47DB-AACD-593F720AFF58", "O2(YsDf&wHTOSAbviFkdP>*C?593y3#ee80%!T4HK;2)5>0A2h") # "https://api.equia.com", "UserId", "AccessSecret")

    input = client.get_unflashed_property_input()
    input.temperature = 550
    input.pressure = 20
    input.components = [
        CalculationComposition(mass=0.78),
        CalculationComposition(mass=0.02),
        CalculationComposition(mass=0.20)
    ]
    input.point_type = "Fixed Temperature/Pressure"

    input.fluid = nHexane_Ethylene_HDPE7()
    input.units = "C(In,Massfraction);C(Out,Massfraction);T(In,Kelvin);T(Out,Kelvin);P(In,Bar);P(Out,Bar);H(In,kJ/Kg);H(Out,kJ/Kg);S(In,kJ/(Kg Kelvin));S(Out,kJ/(Kg Kelvin));Cp(In,kJ/(Kg Kelvin));Cp(Out,kJ/(Kg Kelvin));Viscosity(In,centiPoise);Viscosity(Out,centiPoise);Surfacetension(In,N/m);Surfacetension(Out,N/m)"

    result: ProblemDetails = await client.call_unflashed_properties_async(input)

    await client.cleanup()

    #assert result.status == 400
    assert result.success == True
    assert result.point.volume.units == 'cm3/mole'
    assert result.point.volume.value == 1604.1004460880863
