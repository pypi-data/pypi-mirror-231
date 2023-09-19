import sys
sys.path.append('/Users/tahashmiranda/work-repos/ariksa-policy-cli')
import typer
from ariksa_policy_cli.app.modules.utils.send_request import SendRequest
from ariksa_policy_cli.app.schemas.resource import HTTPMethods, APIResources
import asyncio

app = typer.Typer()


@app.command()
def trigger_discovery(branch: str, account_id:str, shared_secret: str):
    print(branch, shared_secret, account_id)
    s_req = SendRequest(shared_secret=shared_secret)
    import pdb;pdb.set_trace()
    asyncio.run( s_req.send_request(
        method=HTTPMethods.GET,
        resource=APIResources.START_DISCOVERY,
        response_model=str,
        branch=branch,
        shared_secret=shared_secret

    ))

if __name__ == "__main__":
   app()
