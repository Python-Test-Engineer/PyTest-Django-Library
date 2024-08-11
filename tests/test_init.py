from rich.console import Console

console = Console()

# helps separate tests in console output
RESULT_LINE = f"[cyan]{'='*15} RESULT {'='*15}[/]"


def test_init_works():
    console.print("\n[cyan bold]This is test init[/]")
    console.print(RESULT_LINE)
    assert True


def test_init2_works():
    console.print("\n[cyan bold]This is test2 init[/]")
    console.print(RESULT_LINE)
    assert True
