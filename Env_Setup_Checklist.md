# Dev Environment Setup Checklist

- [ ] Install Python
- [ ] Install Git for Windows / Mac
- [ ] Install Cursor (preferred) or VSCode
- [ ] Install Ollama
- [ ] Account Creation – OpenAI
- [ ] Account Creation – GitHub
- [ ] Account Creation – Hugging Face
- [ ] Account Creation – Google Gemini
- [ ] Account Creation – Anthropic
- [ ] License – $5 worth OpenAI Credit 

## Troubleshooting

### Python Installation Issues

#### Windows: Python Not Found in PATH
**Problem**: After installing Python on Windows, the `python` command is not recognized in the terminal.

**Solution**: 
1. Uninstall Python completely
2. Reinstall Python and ensure you check the "Add Python to PATH" option during installation
3. Alternatively, manually add Python to your system PATH environment variable

#### PowerShell Execution Policy Issues
**Problem**: PowerShell throws security errors when trying to execute scripts (e.g., virtual environment activation scripts).

**Solution**: 
1. Open PowerShell as Administrator
2. Run the following command to check current execution policy:
   ```powershell
   Get-ExecutionPolicy
   ```
3. If the policy is "Restricted", change it to allow script execution:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
4. Confirm the change when prompted
5. For virtual environments, you can also use the Command Prompt (cmd) instead of PowerShell 


