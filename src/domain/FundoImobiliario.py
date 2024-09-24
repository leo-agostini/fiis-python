from pydantic import BaseModel

class FundoImobiliario(BaseModel):
  title: str
  setor: str
  valor: float
  liquidezMediaDiaria: float
  pvp: float
  dividendo: float
  yeld: float
  somaYeld3m: float
  somaYeld6m: float
  somaYeld12m: float
  mediaYeld3m: float
  mediaYeld6m: float
  mediaYeld12m: float
  somaYeldAnoCorrente: float
  variacaoCotacaoMes: float
  rentabilidade: float
  rentabilidade_mes: float
  patrimonio: float
  ativos: float
  volatilidade: float
  numeroCotistas: float
  
  def create(self, params):
    return FundoImobiliario(params)
  