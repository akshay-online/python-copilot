# Library Management System - Setup Instructions

## Prerequisites

Before you begin, ensure you have the following installed on your development machine:

### Required Software:
1. **.NET SDK 6.0 or later**
   - Download from: https://dotnet.microsoft.com/download
   - Verify installation: `dotnet --version`

2. **SQL Server** (Choose one)
   - SQL Server 2019+ (Production)
   - SQL Server Express (Free, for development)
   - SQLite (Lightweight, for development)
   
3. **Visual Studio 2022** or **Visual Studio Code**
   - Visual Studio 2022: https://visualstudio.microsoft.com/
   - VS Code: https://code.visualstudio.com/

4. **Git**
   - Download from: https://git-scm.com/downloads

### Optional but Recommended:
- **SQL Server Management Studio (SSMS)** - For database management
- **Postman** - For API testing
- **Docker Desktop** - For containerization (optional)

---

## Step-by-Step Setup

### Step 1: Create the Solution Structure

Open a terminal/command prompt and run the following commands:

```bash
# Create solution directory
mkdir LibraryManagement
cd LibraryManagement

# Create new solution
dotnet new sln -n LibraryManagement

# Create API project (ASP.NET Core Web API)
dotnet new webapi -n LibraryManagement.API -o LibraryManagement.API

# Create Core/Domain project (Class Library)
dotnet new classlib -n LibraryManagement.Core -o LibraryManagement.Core

# Create Application/Business Logic project (Class Library)
dotnet new classlib -n LibraryManagement.Application -o LibraryManagement.Application

# Create Infrastructure/Data Access project (Class Library)
dotnet new classlib -n LibraryManagement.Infrastructure -o LibraryManagement.Infrastructure

# Create Test project (xUnit)
dotnet new xunit -n LibraryManagement.Tests -o LibraryManagement.Tests

# Add all projects to solution
dotnet sln add LibraryManagement.API/LibraryManagement.API.csproj
dotnet sln add LibraryManagement.Core/LibraryManagement.Core.csproj
dotnet sln add LibraryManagement.Application/LibraryManagement.Application.csproj
dotnet sln add LibraryManagement.Infrastructure/LibraryManagement.Infrastructure.csproj
dotnet sln add LibraryManagement.Tests/LibraryManagement.Tests.csproj
```

### Step 2: Set Up Project References

```bash
# API references Application
cd LibraryManagement.API
dotnet add reference ../LibraryManagement.Application/LibraryManagement.Application.csproj
dotnet add reference ../LibraryManagement.Infrastructure/LibraryManagement.Infrastructure.csproj

# Application references Core
cd ../LibraryManagement.Application
dotnet add reference ../LibraryManagement.Core/LibraryManagement.Core.csproj

# Infrastructure references Core
cd ../LibraryManagement.Infrastructure
dotnet add reference ../LibraryManagement.Core/LibraryManagement.Core.csproj

# Tests reference all
cd ../LibraryManagement.Tests
dotnet add reference ../LibraryManagement.API/LibraryManagement.API.csproj
dotnet add reference ../LibraryManagement.Application/LibraryManagement.Application.csproj
dotnet add reference ../LibraryManagement.Infrastructure/LibraryManagement.Infrastructure.csproj
dotnet add reference ../LibraryManagement.Core/LibraryManagement.Core.csproj

cd ..
```

### Step 3: Install NuGet Packages

#### Infrastructure Project:
```bash
cd LibraryManagement.Infrastructure

# Entity Framework Core packages
dotnet add package Microsoft.EntityFrameworkCore
dotnet add package Microsoft.EntityFrameworkCore.SqlServer
dotnet add package Microsoft.EntityFrameworkCore.Design
dotnet add package Microsoft.EntityFrameworkCore.Tools

# For SQLite (development alternative)
dotnet add package Microsoft.EntityFrameworkCore.Sqlite

cd ..
```

#### Application Project:
```bash
cd LibraryManagement.Application

# AutoMapper for DTO mapping
dotnet add package AutoMapper
dotnet add package AutoMapper.Extensions.Microsoft.DependencyInjection

# FluentValidation for validation
dotnet add package FluentValidation
dotnet add package FluentValidation.DependencyInjectionExtensions

cd ..
```

#### API Project:
```bash
cd LibraryManagement.API

# Swagger for API documentation
dotnet add package Swashbuckle.AspNetCore

# Serilog for logging
dotnet add package Serilog.AspNetCore
dotnet add package Serilog.Sinks.Console
dotnet add package Serilog.Sinks.File

cd ..
```

#### Test Project:
```bash
cd LibraryManagement.Tests

# Moq for mocking
dotnet add package Moq
dotnet add package Microsoft.EntityFrameworkCore.InMemory

# FluentAssertions for better test assertions
dotnet add package FluentAssertions

cd ..
```

### Step 4: Build the Solution

```bash
# Build the entire solution
dotnet build

# Expected output: Build succeeded
```

### Step 5: Configure Database Connection

#### For SQL Server:

Edit `LibraryManagement.API/appsettings.json`:

```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=localhost;Database=LibraryManagement;Trusted_Connection=true;TrustServerCertificate=true;"
  },
  "LibrarySettings": {
    "MaxBooksPerMember": 5,
    "LoanPeriodDays": 14,
    "FinePerDay": 1.00,
    "MaxFinePerBook": 50.00,
    "GracePeriodDays": 1,
    "MembershipValidityYears": 1
  },
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning",
      "Microsoft.EntityFrameworkCore": "Warning"
    }
  },
  "AllowedHosts": "*"
}
```

#### For SQLite (Development):

```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Data Source=library.db"
  }
}
```

### Step 6: Create Database Context

Create `LibraryManagement.Infrastructure/Data/LibraryDbContext.cs`:

```csharp
using Microsoft.EntityFrameworkCore;
using LibraryManagement.Core.Entities;

namespace LibraryManagement.Infrastructure.Data
{
    public class LibraryDbContext : DbContext
    {
        public LibraryDbContext(DbContextOptions<LibraryDbContext> options)
            : base(options)
        {
        }

        public DbSet<Book> Books { get; set; }
        public DbSet<Member> Members { get; set; }
        public DbSet<Transaction> Transactions { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            // Configure Book entity
            modelBuilder.Entity<Book>(entity =>
            {
                entity.HasKey(e => e.Id);
                entity.HasIndex(e => e.ISBN).IsUnique();
                entity.Property(e => e.Title).IsRequired().HasMaxLength(200);
                entity.Property(e => e.Author).IsRequired().HasMaxLength(200);
                entity.Property(e => e.Price).HasColumnType("decimal(10,2)");
            });

            // Configure Member entity
            modelBuilder.Entity<Member>(entity =>
            {
                entity.HasKey(e => e.Id);
                entity.HasIndex(e => e.Email).IsUnique();
                entity.HasIndex(e => e.MemberId).IsUnique();
                entity.Property(e => e.FirstName).IsRequired().HasMaxLength(100);
                entity.Property(e => e.LastName).IsRequired().HasMaxLength(100);
                entity.Property(e => e.Email).IsRequired().HasMaxLength(150);
            });

            // Configure Transaction entity
            modelBuilder.Entity<Transaction>(entity =>
            {
                entity.HasKey(e => e.Id);
                entity.HasOne(e => e.Book).WithMany().HasForeignKey(e => e.BookId);
                entity.HasOne(e => e.Member).WithMany().HasForeignKey(e => e.MemberId);
                entity.Property(e => e.FineAmount).HasColumnType("decimal(10,2)");
            });
        }
    }
}
```

### Step 7: Register DbContext in Program.cs

Edit `LibraryManagement.API/Program.cs`:

```csharp
using Microsoft.EntityFrameworkCore;
using LibraryManagement.Infrastructure.Data;
using Serilog;

var builder = WebApplication.CreateBuilder(args);

// Configure Serilog
Log.Logger = new LoggerConfiguration()
    .ReadFrom.Configuration(builder.Configuration)
    .CreateLogger();

builder.Host.UseSerilog();

// Add services to the container.
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// Configure DbContext with SQL Server
builder.Services.AddDbContext<LibraryDbContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection")));

// For SQLite (alternative):
// builder.Services.AddDbContext<LibraryDbContext>(options =>
//     options.UseSqlite(builder.Configuration.GetConnectionString("DefaultConnection")));

// Configure CORS
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowAll", policy =>
    {
        policy.AllowAnyOrigin()
              .AllowAnyMethod()
              .AllowAnyHeader();
    });
});

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();
app.UseCors("AllowAll");
app.UseAuthorization();
app.MapControllers();

app.Run();
```

### Step 8: Create and Apply Migrations

```bash
# Install EF Core tools globally (if not already installed)
dotnet tool install --global dotnet-ef

# Navigate to the Infrastructure project
cd LibraryManagement.Infrastructure

# Create initial migration
dotnet ef migrations add InitialCreate --startup-project ../LibraryManagement.API --context LibraryDbContext

# Apply migration to create database
dotnet ef database update --startup-project ../LibraryManagement.API --context LibraryDbContext

cd ..
```

### Step 9: Run the Application

```bash
# Navigate to API project
cd LibraryManagement.API

# Run the application
dotnet run

# Or watch mode for development (auto-reload on changes)
dotnet watch run
```

The API should now be running at:
- HTTPS: `https://localhost:7xxx`
- HTTP: `http://localhost:5xxx`

Access Swagger UI at: `https://localhost:7xxx/swagger`

---

## Verification Steps

### 1. Verify Database Connection

```bash
# Check if database was created
# In SSMS, refresh databases - you should see "LibraryManagement"
# Or for SQLite, check if "library.db" file exists in API project
```

### 2. Test API Endpoints

Open browser and navigate to: `https://localhost:7xxx/swagger`

You should see the Swagger UI with your API endpoints.

### 3. Run Tests

```bash
# Run all tests
dotnet test

# Run tests with detailed output
dotnet test --verbosity detailed

# Run tests with code coverage
dotnet test /p:CollectCoverage=true
```

---

## Troubleshooting

### Issue: Build Errors

**Solution:**
```bash
# Clean and rebuild
dotnet clean
dotnet restore
dotnet build
```

### Issue: Migration Errors

**Solution:**
```bash
# Remove last migration
dotnet ef migrations remove --startup-project ../LibraryManagement.API

# Re-create migration
dotnet ef migrations add InitialCreate --startup-project ../LibraryManagement.API
```

### Issue: Database Connection Failed

**Solutions:**
1. Check SQL Server is running
2. Verify connection string in appsettings.json
3. Ensure Windows Authentication is enabled (for Trusted_Connection)
4. Try using SQL Server authentication instead:
   ```json
   "Server=localhost;Database=LibraryManagement;User Id=sa;Password=YourPassword;TrustServerCertificate=true;"
   ```

### Issue: Port Already in Use

**Solution:**
Edit `LibraryManagement.API/Properties/launchSettings.json` and change the port numbers.

---

## Development Workflow

### Daily Development:

1. **Pull latest changes:**
   ```bash
   git pull
   ```

2. **Restore packages:**
   ```bash
   dotnet restore
   ```

3. **Run in watch mode:**
   ```bash
   cd LibraryManagement.API
   dotnet watch run
   ```

4. **Run tests:**
   ```bash
   dotnet test
   ```

5. **Create migrations (if model changes):**
   ```bash
   cd LibraryManagement.Infrastructure
   dotnet ef migrations add MigrationName --startup-project ../LibraryManagement.API
   dotnet ef database update --startup-project ../LibraryManagement.API
   ```

---

## Additional Tools

### Useful dotnet CLI Commands:

```bash
# List installed SDKs
dotnet --list-sdks

# List installed runtimes
dotnet --list-runtimes

# Create new controller
dotnet new apicontroller -n BooksController -o Controllers

# Watch for changes and auto-rebuild
dotnet watch

# Generate developer certificate (for HTTPS)
dotnet dev-certs https --trust

# Check for outdated packages
dotnet list package --outdated

# Update packages
dotnet add package PackageName --version x.x.x
```

### EF Core Commands:

```bash
# List all migrations
dotnet ef migrations list

# Remove last migration
dotnet ef migrations remove

# Generate SQL script from migrations
dotnet ef migrations script

# Update to specific migration
dotnet ef database update MigrationName

# Drop database
dotnet ef database drop
```

---

## Next Steps

After successful setup:

1. ✅ Create domain entities in `LibraryManagement.Core/Entities/`
2. ✅ Implement repositories in `LibraryManagement.Infrastructure/Repositories/`
3. ✅ Create services in `LibraryManagement.Application/Services/`
4. ✅ Build API controllers in `LibraryManagement.API/Controllers/`
5. ✅ Write unit tests in `LibraryManagement.Tests/`
6. ✅ Test endpoints using Swagger UI or Postman

---

## Resources

### Documentation:
- ASP.NET Core: https://docs.microsoft.com/aspnet/core
- Entity Framework Core: https://docs.microsoft.com/ef/core
- C# Programming Guide: https://docs.microsoft.com/dotnet/csharp

### Tutorials:
- ASP.NET Core Web API: https://docs.microsoft.com/aspnet/core/tutorials/first-web-api
- EF Core Getting Started: https://docs.microsoft.com/ef/core/get-started

### Community:
- Stack Overflow: https://stackoverflow.com/questions/tagged/asp.net-core
- Reddit: r/dotnet, r/csharp
- Discord: .NET Discord Server

---

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the official documentation
3. Search Stack Overflow
4. Create an issue in the project repository

---

**Happy Coding! 🚀**
