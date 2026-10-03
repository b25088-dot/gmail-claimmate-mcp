from fastapi import FastAPI
from mcp.server.mcpserver import MCPServer

app = FastAPI()
mcp = MCPServer("ClaimMate Gmail")

@mcp.tool()
def search_emails(query: str) -> dict:
    """Search Gmail messages matching a query."""
    return {
        "status": "DEMO",
        "query": query,
        "message": "Gmail search tool connected successfully."
    }

@mcp.tool()
def read_inbox() -> dict:
    """Read recent Gmail messages."""
    return {
        "status": "DEMO",
        "messages": []
    }

@mcp.tool()
def get_thread(thread_id: str) -> dict:
    """Get a Gmail conversation thread."""
    return {
        "status": "DEMO",
        "thread_id": thread_id,
        "messages": []
    }

@mcp.tool()
def send_email(to: str, subject: str, body: str) -> dict:
    """Send an email."""
    return {
        "status": "DEMO",
        "to": to,
        "subject": subject,
        "message": "Email tool connected successfully."
    }

app = mcp.streamable_http_app()
