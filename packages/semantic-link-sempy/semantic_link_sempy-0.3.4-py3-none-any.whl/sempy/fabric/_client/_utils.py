import os
import sys
from pathlib import Path


_analysis_services_initialized = False


def _init_analysis_services() -> None:
    global _analysis_services_initialized
    if _analysis_services_initialized:
        return

    from clr_loader import get_coreclr
    from pythonnet import set_runtime

    my_path = Path(__file__).parent

    rt = get_coreclr(runtime_config=os.fspath(my_path / ".." / ".." / "dotnet.runtime.config.json"))
    set_runtime(rt)

    import clr
    assembly_path = my_path / ".." / ".." / "lib"

    sys.path.append(os.fspath(assembly_path))
    clr.AddReference(os.fspath(assembly_path / "Microsoft.AnalysisServices.Tabular.dll"))
    clr.AddReference(os.fspath(assembly_path / "Microsoft.AnalysisServices.AdomdClient.dll"))
    clr.AddReference(os.fspath(assembly_path / "SemPyParquetWriter.dll"))

    _analysis_services_initialized = True
