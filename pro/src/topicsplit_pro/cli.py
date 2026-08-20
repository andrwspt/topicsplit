"""CLI for TopicSplit Pro."""

import sys
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

from .splitter import split_text, render_markdown
from . import __version__

console = Console()


@click.group()
@click.version_option(version=__version__, prog_name="topicsplit")
def cli():
    """TopicSplit Pro — batch semantic text grouper.

    Split articles, transcripts, and notes into topic segments by meaning.
    """
    pass


@cli.command()
@click.argument("input_file", type=click.Path(exists=True, dir_okay=False))
@click.option("-o", "--output", type=click.Path(dir_okay=False), help="Output file (default: INPUT_topicsplit.md)")
@click.option("-s", "--sensitivity", type=float, default=0.55, show_default=True, help="0.0 = fewer segments, 1.0 = more segments")
@click.option("--no-skip-tiny", is_flag=True, help="Don't merge tiny segments")
@click.option("--stdout", is_flag=True, help="Print to stdout instead of file")
def split(input_file, output, sensitivity, no_skip_tiny, stdout):
    """Split a single file into topic segments."""
    text = Path(input_file).read_text(encoding="utf-8")
    if not text.strip():
        console.print("[red]Error:[/red] Input file is empty.")
        sys.exit(1)

    segments = split_text(text, sensitivity=sensitivity, skip_tiny=not no_skip_tiny)
    md = render_markdown(segments)

    if stdout:
        console.print(md)
    else:
        out_path = output or input_file.replace(".txt", "_topicsplit.md").replace(".md", "_topicsplit.md")
        Path(out_path).write_text(md, encoding="utf-8")
        console.print(f"[green]✓[/green] {len(segments)} segments → {out_path}")

    # Summary table
    table = Table(title="Segments", show_header=True, header_style="bold")
    table.add_column("Topic", style="cyan")
    table.add_column("Sentences", justify="right", style="green")
    table.add_column("Preview", style="white")
    for i, (seg, n) in enumerate(segments):
        preview = seg.split("\n")[1][:60] + "..." if len(seg) > 60 else seg
        table.add_row(str(i + 1), str(n), preview)
    console.print(table)


@cli.command()
@click.argument("input_dir", type=click.Path(exists=True, file_okay=False))
@click.option("-o", "--output-dir", type=click.Path(file_okay=False), help="Output directory (default: INPUT_topicsplit/)")
@click.option("-s", "--sensitivity", type=float, default=0.55, show_default=True, help="0.0 = fewer segments, 1.0 = more segments")
@click.option("--ext", default=".txt", show_default=True, help="File extension to process")
@click.option("--recursive", "-r", is_flag=True, help="Process subdirectories")
def batch(input_dir, output_dir, sensitivity, ext, recursive):
    """Batch-split all files in a directory."""
    in_path = Path(input_dir)
    out_path = Path(output_dir) if output_dir else in_path.parent / f"{in_path.name}_topicsplit"
    out_path.mkdir(exist_ok=True)

    pattern = f"**/*{ext}" if recursive else f"*{ext}"
    files = list(in_path.glob(pattern))
    if not files:
        console.print(f"[yellow]No {ext} files found in {input_dir}[/yellow]")
        sys.exit(0)

    console.print(f"[bold]Processing {len(files)} files...[/bold]")
    total_segs = 0
    for f in files:
        text = f.read_text(encoding="utf-8")
        if not text.strip():
            continue
        segments = split_text(text, sensitivity=sensitivity)
        md = render_markdown(segments)
        out_file = out_path / f"{f.stem}_topicsplit.md"
        out_file.write_text(md, encoding="utf-8")
        total_segs += len(segments)
        console.print(f"  [green]✓[/green] {f.name} → {len(segments)} segments")

    console.print(f"\n[bold green]Done:[/bold green] {len(files)} files, {total_segs} total segments → {out_path}")


@cli.command()
@click.argument("text")
@click.option("-s", "--sensitivity", type=float, default=0.55, show_default=True, help="0.0 = fewer segments, 1.0 = more segments")
def echo(text, sensitivity):
    """Split inline text and print to stdout."""
    segments = split_text(text, sensitivity=sensitivity)
    md = render_markdown(segments)
    console.print(md)


if __name__ == "__main__":
    cli()
