// Write a function to get the latest commits from a GitHub repository
// using the GitHub API.
// write the committer name, commit message and the date into an excel file in one sheet

using System;
using System.Collections.Generic;
using System.IO;
using OfficeOpenXml;
using System.Net.Http;
using System.Net.Http.Headers;

namespace GitHubCommitsToExcel
{
    class Program
    {
        static void Main(string[] args)
        {
            string repoOwner = "octocat"; // Replace with the repository owner
            string repoName = "Hello-World"; // Replace with the repository name
            string excelFilePath = "GitHubCommits.xlsx";

            var commits = GetLatestCommits(repoOwner, repoName).Result;
            WriteCommitsToExcel(commits, excelFilePath);
            Console.WriteLine($"Commits written to {excelFilePath}");
        }

        public class CommitInfo
        {
            public string CommitterName { get; set; }
            public string CommitMessage { get; set; }
            public DateTime CommitDate { get; set; }
        }

        static async System.Threading.Tasks.Task<List<CommitInfo>> GetLatestCommits(string owner, string repo)
        {
            var commits = new List<CommitInfo>();
            using (var client = new HttpClient())
            {
                client.BaseAddress = new Uri("https://api.github.com/");
                client.DefaultRequestHeaders.UserAgent.Add(new ProductInfoHeaderValue("Mozilla", "5.0"));
                client.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/vnd.github.v3+json"));

                var response = await client.GetAsync($"/repos/{owner}/{repo}/commits");
                response.EnsureSuccessStatusCode();

                var commitData = await response.Content.ReadAsAsync<dynamic[]>();

                foreach (var item in commitData)
                {
                    try
                    {
                        commits.Add(new CommitInfo
                        {
                            CommitterName = item?.commit?.committer?.name ?? "Unknown",
                            CommitMessage = item?.commit?.message ?? "No message",
                            CommitDate = item?.commit?.committer?.date != null 
                                ? DateTime.Parse(item.commit.committer.date.ToString()) 
                                : DateTime.MinValue
                        });
                    }
                    catch (Exception ex)
                    {
                        // Log the error and continue with default values
                        Console.WriteLine($"Error processing commit: {ex.Message}");
                        commits.Add(new CommitInfo
                        {
                            CommitterName = "Error",
                            CommitMessage = "Failed to parse commit data",
                            CommitDate = DateTime.MinValue
                        });
                    }
                }
            }
            return commits;
        }

        static void WriteCommitsToExcel(List<CommitInfo> commits, string filePath)
        {
            ExcelPackage.LicenseContext = LicenseContext.NonCommercial;
            using (var package = new ExcelPackage())
            {
                var worksheet = package.Workbook.Worksheets.Add("Commits");
                worksheet.Cells[1, 1].Value = "Committer Name";
                worksheet.Cells[1, 2].Value = "Commit Message";
                worksheet.Cells[1, 3].Value = "Commit Date";

                for (int i = 0; i < commits.Count; i++)
                {
                    worksheet.Cells[i + 2, 1].Value = commits[i].CommitterName;
                    worksheet.Cells[i + 2, 2].Value = commits[i].CommitMessage;
                    worksheet.Cells[i + 2, 3].Value = commits[i].CommitDate.ToString("yyyy-MM-dd HH:mm:ss");
                }
                package.SaveAs(new FileInfo(filePath));
            }
        }
    }
}