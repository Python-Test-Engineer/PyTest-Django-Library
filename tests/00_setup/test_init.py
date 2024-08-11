from rich.console import Console

console = Console()

def test_init_works():
    console.print("\n[cyan bold]This is test init[/]")
    assert True


def test_init2_works():
    console.print("\n[cyan bold]This is test2 init[/]")
    assert True
