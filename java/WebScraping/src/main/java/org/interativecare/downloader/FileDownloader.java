package org.interativecare.downloader;

import java.io.BufferedInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.nio.file.Path;

public class FileDownloader {
    // Metodo para baixar os arquivos PDF do site
    public static void downloadFile(String fileUrl, Path destination){
        try {
            BufferedInputStream in = new BufferedInputStream(new URL(fileUrl).openStream());
            FileOutputStream fileOutputStream = new FileOutputStream(destination.toFile());
            byte[] buffer = new byte[1024];
            int bytesRead;
            while ((bytesRead = in.read(buffer, 0, 1024)) != -1) {
                fileOutputStream.write(buffer, 0, bytesRead);
            }
        }catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        } catch (MalformedURLException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
