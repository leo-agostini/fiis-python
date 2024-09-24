from pyppeteer import launch
from ...application.service.FiiScrappingService import FiiScrappingService
from ...domain.FundoImobiliario import FundoImobiliario


class PyppeteerFiiScrappingService(FiiScrappingService):
    async def scrapFiis() -> FundoImobiliario:
        browser=await launch(options={'args': ['--no-sandbox', '--headless']})
        page = await browser.newPage()
        await page.goto("https://www.fundsexplorer.com.br/ranking")
        await page.waitForSelector('.default-fiis-table__container__table__body > tr')
        rows = await page.evaluate('''() => {
        const rows = document.querySelectorAll('.default-fiis-table__container__table__body > tr');
        return Array.from(rows).map(row => {
            const columns = row.querySelectorAll('td');
            const data = {};
            columns.forEach(col => {
                const key = col.getAttribute('data-collum');
                const value = col.getAttribute('data-value');
                data[key] = value ? value.trim() : null;
            });
            return data;
        });
        }''')
        print(rows)
        await browser.close()
        fundos = []
        for row in rows:
            try:
                fundo = FundoImobiliario(
                    title=row.get("collum-post_title", ""),
                    setor=row.get("collum-setor", ""),
                    valor=float(row.get("collum-valor", "0").replace(',', '.')),
                    liquidezMediaDiaria=float(row.get("collum-liquidezmediadiaria", "0").replace('.', '').replace(',', '.')),
                    pvp=float(row.get("collum-pvp", "0").replace(',', '.')),
                    dividendo=float(row.get("collum-dividendo", "0").replace(',', '.')),
                    yeld=float(row.get("collum-yeld", "0").replace(',', '.')),
                    somaYeld3m=float(row.get("collum-soma_yield_3m", "0").replace(',', '.')),
                    somaYeld6m=float(row.get("collum-soma_yield_6m", "0").replace(',', '.')),
                    somaYeld12m=float(row.get("collum-soma_yield_12m", "0").replace(',', '.')),
                    mediaYeld3m=float(row.get("collum-media_yield_3m", "0").replace(',', '.')),
                    mediaYeld6m=float(row.get("collum-media_yield_6m", "0").replace(',', '.')),
                    mediaYeld12m=float(row.get("collum-media_yield_12m", "0").replace(',', '.')),
                    somaYeldAnoCorrente=float(row.get("collum-soma_yield_ano_corrente", "0").replace(',', '.')),
                    variacaoCotacaoMes=float(row.get("collum-variacao_cotacao_mes", "0").replace(',', '.')),
                    rentabilidade=float(row.get("collum-rentabilidade", "0").replace(',', '.')),
                    rentabilidade_mes=float(row.get("collum-rentabilidade_mes", "0").replace(',', '.')),
                    patrimonio=float(row.get("collum-patrimonio", "0").replace('.', '').replace(',', '.')),
                    ativos=float(row.get("collum-ativos", "0").replace('.', '').replace(',', '.')),
                    volatilidade=float(row.get("collum-volatility", "0").replace(',', '.')),
                    numeroCotistas=float(row.get("collum-numero_cotista", "0").replace('.', '').replace(',', '.'))
                )
                fundos.append(fundo)
            except Exception as e:
                print(f"Error processing row: {e}")
            return fundos


        
        
         