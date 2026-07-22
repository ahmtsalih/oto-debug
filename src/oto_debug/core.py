import subprocess
import os
from rich.console import Console
from .ai import analyze_error

console = Console()

def execute_and_listen(command_args: list):
    full_command = list(command_args)
    
    # Windows'ta doğrudan .py çalıştırılamadığı için araya python ekliyoruz
    if full_command[0].endswith(".py"):
        full_command.insert(0, "python")
        
    command_str = " ".join(full_command)
    
    try:
        process = subprocess.run(full_command, capture_output=True, text=True)
        
        if process.returncode != 0:
            with console.status("[bold cyan]🤖 Yapay Zeka hatayı inceliyor...[/bold cyan]", spinner="dots"):
                ai_response = analyze_error(command_str, process.stderr)
            return False, process.stderr, ai_response
        
        return True, process.stdout, None
        
    except FileNotFoundError:
        return False, "COMMAND_NOT_FOUND", None
    except Exception as e:
        return False, str(e), None