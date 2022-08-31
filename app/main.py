"""  DEMO FASTAPI SOLUCIONES ANDINAS """

from typing import Union
from enum import Enum

from fastapi import FastAPI , Query, Form, Path
from pydantic import BaseModel, HttpUrl, Field

class Producto(BaseModel):
    nombre: str =Field(example="Plazo Fijo Regulado")
    descripcion: str | None = Field(default=None, example="con tasa regulada")
    importe: float = Field(example=1050.89)
    tasa: float | None = Field(default=None, example=7.9)
    periodos: set[str] = Field([ 
           "Anual", "Semestral", "Mensual" ])

class Foto(BaseModel):
    url: HttpUrl
    name: str

class Cliente(BaseModel):
    name: str
    full_name: str | None = None
    foto: Foto | None = None 

app = FastAPI()


@app.post("/productos/")
async def Calcular_Importe(item: Producto):
    item_dict = item.dict()
    if item.tasa:
        importe_calculado = item.importe + item.tasa
        item_dict.update({"importe calculado": importe_calculado})
    return item_dict

@app.get("/productos/")
async def Leer_cosas(
    q: Union[str, None] = Query(
        default=None,
        alias="item-query",
        title="Cadena de Consulta",
        description="Cadena para buscar en productos ",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.put("/productos/{item_id}") 
async def update_input(
    *,
    item_id: int = Path(title="El Nro de Producto", ge=0, le=1000),
    q: str | None = None,
    item: Producto | None = None, 
    cliente: Cliente
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    results.update({"Cliente": cliente})    
    return results

@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}