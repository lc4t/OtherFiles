import java.net.*;
import java.io.*;
import java.nio.file.*;

public class visit
{
    /*
    * visit: `http://www.bbc.co.uk/search` post with urlencode(ascii) `q=java`
    *         set `content-type: application/x-www-form-urlencoded`
    * open connection
    *         set not follow redirects, if happen(301/302), print `Moved to NEWURL`
    *         set request headers params and need output
    * get OutputStream from connection output
    *         judge response status code, handle 301/302
    *         if not 301/302, write source code to file `bbc.txt`
    */
    public static void main (String[] args) throws Exception
    {
        URL url = new URL("http://www.bbc.co.uk/search");
        String rawData = "q=java";
        String encodedData = URLEncoder.encode(rawData, "ASCII");
        String contentType = "application/x-www-form-urlencoded";
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setInstanceFollowRedirects(false);
        conn.setRequestMethod("POST");
        conn.setRequestProperty("contentType", contentType);
        conn.setRequestProperty("Content-Length", String.valueOf(encodedData.length()));
        conn.setDoOutput(true);
        OutputStream os = conn.getOutputStream();
        os.write(encodedData.getBytes());
        int response = conn.getResponseCode();
        if (response == HttpURLConnection.HTTP_MOVED_PERM || response == HttpURLConnection.HTTP_MOVED_TEMP)
        {
            System.out.println("Moved to: " + conn.getHeaderField("Location"));
        }
        else
        {
            try (InputStream in = conn.getInputStream())
            {
                Files.copy(in, Paths.get("bbc.txt"), StandardCopyOption.REPLACE_EXISTING);
            }
        }
    }
}
