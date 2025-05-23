import sys
import asyncio


# Main entry point for the CLI when installed as a package
def cli_entry_point():
    """
    Entry point for the CLI tool when installed via pip
    """
    # Import here to avoid circular imports
    from k8s_assistant.client import async_main
    
    try:
        asyncio.run(async_main())
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    cli_entry_point()
