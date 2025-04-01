package org.interativecare;

import org.interativecare.compressor.ZipCompressor;
import org.interativecare.downloader.FileDownloader;
import org.interativecare.downloader.PdfDownloader;

import java.io.File;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        try (Scanner scan = new Scanner(System.in)) {
            System.out.println("Digite o caminho para salvar os arquivos: ");
            String path = scan.nextLine();

            Path downloadDir = prepareDirectory(path);

            List<String> pdfLinks = PdfDownloader.getPdfLinks();
            List<File> downloadedFiles = downloadFiles(pdfLinks, downloadDir);

            File zipFile = createZipFile(downloadDir, downloadedFiles);
            System.out.println("Compactação concluída: " + zipFile.getAbsolutePath());
        }
    }
    // Metodo para preparar o diretório.
    private static Path prepareDirectory(String path) {
        Path downloadDir = Paths.get(path);
        if (!downloadDir.toFile().exists()) {
            downloadDir.toFile().mkdirs();
        }
        return downloadDir;
    }

    // Metodo para baixar os PDFs.
    private static List<File> downloadFiles(List<String> pdfLinks, Path downloadDir) {
        List<File> downloadedFiles = new ArrayList<>();
        for (String pdfUrl : pdfLinks) {
            try {
                String fileName = pdfUrl.substring(pdfUrl.lastIndexOf("/") + 1);
                Path destination = downloadDir.resolve(fileName);
                System.out.println("Baixando: " + pdfUrl);
                FileDownloader.downloadFile(pdfUrl, destination);
                downloadedFiles.add(destination.toFile());
            } catch (Exception e) {
                System.err.println("Erro ao baixar o arquivo " + pdfUrl + ": " + e.getMessage());
            }
        }
        return downloadedFiles;
    }

    // Metodo para compactar.
    private static File createZipFile(Path downloadDir, List<File> downloadedFiles) {
        File zipFile = new File(downloadDir.toFile(), "Anexos.zip");
        ZipCompressor.zipFiles(downloadedFiles, zipFile);
        return zipFile;
    }
}