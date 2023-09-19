import pytest
from equia.models import CalculationComposition, CloudPointCalculationType, ProblemDetails, ApiCallResult 
from equia.equia_client import EquiaClient
from equia.demofluids.fluids import nHexane_Ethylene_HDPE7

@pytest.mark.asyncio
async def test_call_cloudpoint():
    client = EquiaClient(
      "https://localhost:5201", "760C278E-20F7-4E31-AD0E-D0CF564D1414", "##glD47#al!=(d+53ES3?qW") # "https://api.equia.com", "UserId", "AccessSecret")

    input = client.get_cloud_point_input()
    input.pressure = 30
    input.components = [
        CalculationComposition(mass=0.78),
        CalculationComposition(mass=0.02),
        CalculationComposition(mass=0.20)
    ]
    input.point_type = CloudPointCalculationType.FIXED_PRESSURE

    input.fluid = nHexane_Ethylene_HDPE7()
    input.units = "C(In,Massfraction);C(Out,Massfraction);T(In,Kelvin);T(Out,Kelvin);P(In,Bar);P(Out,Bar);H(In,kJ/Kg);H(Out,kJ/Kg);S(In,kJ/(Kg Kelvin));S(Out,kJ/(Kg Kelvin));Cp(In,kJ/(Kg Kelvin));Cp(Out,kJ/(Kg Kelvin));Viscosity(In,centiPoise);Viscosity(Out,centiPoise);Surfacetension(In,N/m);Surfacetension(Out,N/m)"

    result: ProblemDetails = await client.call_cloud_point_async(input)

    await client.cleanup()

    #assert result.status == 400
    assert result.api_status == ApiCallResult.SUCCESS
    assert len(result.point.phases) == 2
