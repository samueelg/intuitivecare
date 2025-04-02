import tabula
import pandas as pd
import zipfile
import os

def convert_pdf_to_csv(pdf_path: str, output_csv: str = None):
    try:
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"O arquivo {pdf_path} não existe.");
        
        if output_csv is None:
            output_csv = os.path.splitext(pdf_path)[0] + ".csv"
        
        # Lê o PDF e converte para DataFrame
        dfs = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True, lattice=True, stream=True)

        if not dfs:
            raise ValueError("Nenhuma tabela encontrada no PDF.");
    
        combined_df = pd.concat(dfs, ignore_index=True)

        if "Unnamed: 0" in combined_df.columns:
            combined_df = combined_df.drop(columns=["Unnamed: 0"])

        combined_df.to_csv(output_csv, index=False, encoding="utf-8-sig")

        #Compacta o arquivo CSV em um arquivo ZIP, com o nome "Teste_Samuel.zip"
        zip_path = os.path.join(os.path.dirname(output_csv), "Teste_Samuel.zip")
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(output_csv, os.path.basename(output_csv))
        
        print(f"Arquivo ZIP criado: {zip_path}")

        print(f"Arquivo CSV gerado com sucesso: {output_csv}")
    except Exception as e:
        print(f"Erro: {e}");

def rename_csv_columns(csv_path: str, column_mapping: dict, output_csv: str = None):
    try:
        df = pd.read_csv(csv_path)
        if any(idx >= len(df.columns) or idx < 0 for idx in column_mapping.keys()):
            raise ValueError("Índice de coluna inválido na renomeação.")
        
        for idx, new_name in column_mapping.items():
            df.columns.values[idx] = new_name

        if output_csv is None:
            output_csv = csv_path

        df.to_csv(csv_path, index=False, encoding="utf-8-sig")
        print(f"Colunas renomeadas com sucesso no arquivo: {csv_path}")

    except FileNotFoundError:
        print(f"Erro: O arquivo {csv_path} não foi encontrado.")
    except pd.errors.EmptyDataError:
        print(f"Erro: O arquivo {csv_path} está vazio.")
    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        print(f"Erro: {e}")

def main():
    pdf_path = input("Digite o caminho do arquivo PDF: ").strip()
    convert_pdf_to_csv(pdf_path)
    rename_csv_columns(pdf_path.replace(".pdf", ".csv"), {3: "Odontológica", 4: "Ambulatorial"})

if __name__ == "__main__":
    main()





