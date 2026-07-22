import typer
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from typing import List
from .config import save_api_key
from .core import execute_and_listen

app = typer.Typer(help="oto-debug: Yapay Zeka Destekli Hata Ayıklayıcı")
console = Console()

@app.command("kur")
def setup(api_key: str = typer.Argument(..., help="Gemini API Anahtarı")):
    save_api_key(api_key)
    console.print(Panel("[bold green]✅ API Anahtarı başarıyla kaydedildi![/bold green]", border_style="green"))

@app.command("run", context_settings={"allow_extra_args": True, "ignore_unknown_options": True})
def run(ctx: typer.Context):
    command_args = ctx.args
    if not command_args:
        console.print("[bold red]Hata: Çalıştırılacak bir komut girmelisiniz.[/bold red]")
        raise typer.Exit(code=1)

    console.print(f"[bold blue]🚀 Çalıştırılıyor:[/bold blue] {' '.join(command_args)}")
    console.print("-" * 40)

    success, output, ai_response = execute_and_listen(command_args)

    if success:
        console.print(output)
    else:
        if output == "COMMAND_NOT_FOUND":
            console.print(f"[bold red]Hata:[/bold red] '{command_args[0]}' komutu bulunamadı.")
            raise typer.Exit(code=1)
            
        console.print(Panel(output, title="[bold red]🚨 YAKALANAN HATA[/bold red]", border_style="red"))
        
        if ai_response == "API_KEY_MISSING":
            console.print("[bold yellow]Yapay zeka analizi için API anahtarı eksik. Lütfen 'oto-debug kur <API_KEY>' komutu ile kurulum yapın.[/bold yellow]")
        elif ai_response and ai_response.startswith("AI_ERROR"):
            console.print(f"[bold red]Yapay zeka bağlantı hatası:[/bold red] {ai_response}")
        elif ai_response:
            md = Markdown(ai_response)
            console.print(Panel(md, title="[bold green]💡 AI ÇÖZÜM ÖNERİSİ[/bold green]", border_style="green"))

def main():
    app()