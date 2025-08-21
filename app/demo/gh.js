const { Octokit } = require('@octokit/rest');
const XLSX = require('xlsx');
const path = require('path');

async function getGitHubCommits(owner, repo, maxCommits = 30) {
    try {
        // Initialize Octokit
        const octokit = new Octokit({
            auth: process.env.GITHUB_TOKEN // Make sure to set your GitHub token as environment variable
        });

        // Fetch commits
        const response = await octokit.repos.listCommits({
            owner,
            repo,
            per_page: maxCommits
        });

        // Extract relevant commit data
        const commitData = response.data.map(commit => ({
            committer: commit.commit.committer.name,
            message: commit.commit.message,
            date: commit.commit.committer.date
        }));

        // Create workbook and worksheet
        const wb = XLSX.utils.book_new();
        const ws = XLSX.utils.json_to_sheet(commitData);

        // Set column widths
        const colWidths = [
            { wch: 20 }, // committer name
            { wch: 50 }, // commit message
            { wch: 20 }  // date
        ];
        ws['!cols'] = colWidths;

        // Add worksheet to workbook
        XLSX.utils.book_append_sheet(wb, ws, 'Commits');

        // Generate output filename
        const outputPath = path.join(__dirname, `${owner}-${repo}-commits.xlsx`);

        // Write to file
        XLSX.writeFile(wb, outputPath);

        console.log(`Excel file created successfully at: ${outputPath}`);
        return outputPath;
    } catch (error) {
        console.error('Error fetching commits:', error.message);
        throw error;
    }
}

// Example usage
module.exports = getGitHubCommits;

// You can test the function like this:
// getGitHubCommits('owner', 'repo-name');

