from typing_extensions import Annotated
import openai
import typer


app = typer.Typer(add_completion=False)


embedding_models = [
    'text-embedding-ada-002',
]

completion_models = [
    'gpt-3.5-turbo-instruct',
    'davinci-002',
    'babbage-002',
]

chat_completion_models = [
    'gpt-4-0613',
    'gpt-4',
    'gpt-3.5-turbo-instruct-0914',
    'gpt-3.5-turbo-0613',
    'gpt-3.5-turbo-0301',
    'gpt-3.5-turbo-16k',
    'gpt-3.5-turbo',
    'gpt-4-0314',
    'gpt-3.5-turbo-16k-0613',
]


@app.callback()
def callback():
    """
    shellm = shell + LLM
    """


@app.command()
def completion(
    prompt: str,
    model: str="gpt-3.5-turbo-instruct",
    temperature: Annotated[float, typer.Option(help="Sampling temperature between 0 and 2.")] = 0.8,
    top_p: Annotated[float, typer.Option(help="Nucleus sampling parameter between 0 and 1.")] = 1.0,
    max_tokens: int=512,
    stream: bool=False,
):
    """
    A completion
    https://platform.openai.com/docs/api-reference/completions
    """
    completion = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        stream=stream,
    )
    if stream:
        for piece in completion:
            typer.echo(piece.choices[0]["text"], nl=False)
    else:
        typer.echo(completion.choices[0]["text"])


@app.command()
def chat_completion(
    user_message: str,
    model: str="gpt-3.5-turbo",
    temperature: Annotated[float, typer.Option(help="Sampling temperature between 0 and 2.")] = 0.8,
    top_p: Annotated[float, typer.Option(help="Nucleus sampling parameter between 0 and 1.")] = 1.0,
    max_tokens: int=512,
    stream: bool=False,
):
    """
    A chat completion
    https://platform.openai.com/docs/api-reference/chat
    """
    completion = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "user", "content": user_message}
        ],
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        stream=stream,
    )
    if stream:
        for piece in completion:
            typer.echo(piece.choices[0]['delta'].get("content", "\n"), nl=False)
    else:
        typer.echo(completion.choices[0].message.content)





@app.command()
def load():
    """
    Load the portal gun
    """
    typer.echo("Loading portal gun")
