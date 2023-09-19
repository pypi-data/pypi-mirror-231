from pimp.common import *

from .lsp import run_lsp
from .ts import run_ts

console = rich.console.Console()

@click.group()
@click.option("--debug/--no-debug", default=False)
@click.option(
    "--profile", is_flag=True, default=False, help="Enable profiling using cProfile."
)
@click.version_option(message="%(version)s", package_name="woke")
@click.pass_context
def main(ctx: click.core.Context, debug: bool, profile: bool) -> None:
    if profile:
        import atexit
        import cProfile

        pr = cProfile.Profile()
        pr.enable()

        def exit():
            pr.disable()
            pr.dump_stats("woke.prof")

        atexit.register(exit)

    rich.traceback.install(show_locals=debug, suppress=[click], console=console)
    logging.basicConfig(
        format="%(asctime)s %(name)s: %(message)s",
        handlers=[rich.logging.RichHandler(show_time=False, console=console)],
        level=(logging.WARNING if not debug else logging.DEBUG),
    )

    ctx.ensure_object(dict)
    ctx.obj["debug"] = debug

    os.environ["PYTHONBREAKPOINT"] = "pdbr.set_trace"


main.add_command(run_lsp)
main.add_command(run_ts)
