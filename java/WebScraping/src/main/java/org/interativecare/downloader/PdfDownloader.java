package org.interativecare.downloader;

import org.jsoup.HttpStatusException;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class PdfDownloader {
    private static final String URL_BASE = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos";

    // Metodo para salvar os PDFs em uma Lista dinamica
    public static List<String> getPdfLinks() {
        List<String> pdfLinks = new ArrayList<>();
        Document doc = null;
        try {
            doc = Jsoup.connect(URL_BASE).get();

        // Procura por links clicaveis que contenham ".pdf"
        for (Element link : doc.select("a[href$=.pdf]")) {
            String pdfUrl = link.absUrl("href");
            String linkText = link.text().toLowerCase();

            // Armazena apenas os PDFs que se chamem "Anexo I" e "Anexo II"
            if (linkText.contains("anexo i") || linkText.contains("anexo ii")) {
                pdfLinks.add(pdfUrl);
                System.out.println("PDF encontrado: " + linkText + " -> " + pdfUrl);
            }
        }
        }  catch (HttpStatusException e) {
            System.err.println("Erro HTTP ao acessar URL: " + e.getMessage() +
                    " (Status code: " + e.getStatusCode() + ")");
        } catch (IOException e) {
            System.err.println("Erro de I/O ao acessar URL: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("Erro inesperado: " + e.getMessage());
        }
        return pdfLinks;
    }
}
