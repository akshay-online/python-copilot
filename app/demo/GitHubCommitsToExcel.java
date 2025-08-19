// You need to add dependencies for Apache POI and a JSON library like org.json or Jackson.

// filepath: src/main/java/com/example/GitHubCommitsToExcel.java
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;
import org.json.JSONArray;
import org.json.JSONObject;

import java.io.FileOutputStream;
import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;

public class GitHubCommitsToExcel {

    public static JSONArray getLatestCommits(String repo, String token, int numCommits) throws IOException {
        String apiUrl = String.format("https://api.github.com/repos/%s/commits?per_page=%d", repo, numCommits);
        URL url = new URL(apiUrl);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestProperty("Authorization", "token " + token);
        conn.setRequestMethod("GET");

        int responseCode = conn.getResponseCode();
        if (responseCode != 200) {
            throw new IOException("Failed to fetch commits: " + responseCode);
        }

        Scanner scanner = new Scanner(conn.getInputStream());
        StringBuilder json = new StringBuilder();
        while (scanner.hasNext()) {
            json.append(scanner.nextLine());
        }
        scanner.close();

        return new JSONArray(json.toString());
    }

    public static void saveCommitsToExcel(JSONArray commits, String filename) throws IOException {
        Workbook workbook = new XSSFWorkbook();
        Sheet sheet = workbook.createSheet("Commits");

        Row header = sheet.createRow(0);
        header.createCell(0).setCellValue("Committer Name");
        header.createCell(1).setCellValue("Commit Message");

        for (int i = 0; i < commits.length(); i++) {
            JSONObject commitObj = commits.getJSONObject(i).getJSONObject("commit");
            String committerName = commitObj.getJSONObject("committer").getString("name");
            String commitMessage = commitObj.getString("message");

            Row row = sheet.createRow(i + 1);
            row.createCell(0).setCellValue(committerName);
            row.createCell(1).setCellValue(commitMessage);
        }

        try (FileOutputStream fileOut = new FileOutputStream(filename)) {
            workbook.write(fileOut);
        }
        workbook.close();
    }

    public static void main(String[] args) throws IOException {
        String repo = "owner/repo"; // Replace with your repo
        String token = "your-personal-access-token"; // Replace with your token
        int numCommits = 10;

        JSONArray commits = getLatestCommits(repo, token, numCommits);
        saveCommitsToExcel(commits, "latest_commits.xlsx");
    }
}