# Library Management System - Quick Start Guide

This guide will help you get the Library Management System MVP up and running quickly.

## 🚀 Quick Start (5 Minutes)

### Option 1: Using Visual Studio 2022

1. **Create New Project**
   - Open Visual Studio 2022
   - Click "Create a new project"
   - Select "ASP.NET Core Web API"
   - Name it: `LibraryManagement`
   - Choose .NET 6.0 or later
   - Check "Use controllers" and "Enable OpenAPI support"

2. **Install Required Packages**
   - Right-click on project → Manage NuGet Packages
   - Install these packages:
     - `Microsoft.EntityFrameworkCore.SqlServer`
     - `Microsoft.EntityFrameworkCore.Tools`
     - `Microsoft.EntityFrameworkCore.Design`
     - `Swashbuckle.AspNetCore` (should be pre-installed)

3. **Build and Run**
   - Press F5 or click the green Run button
   - Swagger UI will open automatically

### Option 2: Using Command Line (Fastest)

```bash
# 1. Create project
dotnet new webapi -n LibraryManagement
cd LibraryManagement

# 2. Add packages
dotnet add package Microsoft.EntityFrameworkCore.SqlServer
dotnet add package Microsoft.EntityFrameworkCore.Tools
dotnet add package Microsoft.EntityFrameworkCore.Design

# 3. Run
dotnet run
```

Visit: `https://localhost:7xxx/swagger`

---

## 📝 MVP Checklist

### Core Entities (30 minutes)
- [ ] Create `Book.cs` model
- [ ] Create `Member.cs` model
- [ ] Create `Transaction.cs` model

### Database Setup (20 minutes)
- [ ] Create `LibraryDbContext.cs`
- [ ] Configure connection string
- [ ] Create initial migration
- [ ] Update database

### API Controllers (2 hours)
- [ ] `BooksController` - CRUD operations
- [ ] `MembersController` - CRUD operations
- [ ] `TransactionsController` - Issue/Return logic

### Business Logic (2 hours)
- [ ] Book availability check
- [ ] Member validation
- [ ] Due date calculation
- [ ] Fine calculation

### Testing (1 hour)
- [ ] Test all API endpoints
- [ ] Verify business rules
- [ ] Check error handling

---

## 🎯 MVP Features Priority

### Week 1 - Foundation
**Day 1-2: Setup & Models**
- ✅ Create solution structure
- ✅ Define domain entities
- ✅ Set up database

**Day 3-4: Books Management**
- ✅ Add Book CRUD API
- ✅ Search functionality
- ✅ Test endpoints

**Day 5: Members Management**
- ✅ Add Member CRUD API
- ✅ Member search
- ✅ Test endpoints

### Week 2 - Core Features
**Day 1-3: Transactions**
- ✅ Issue book logic
- ✅ Return book logic
- ✅ Validation rules

**Day 4-5: Testing & Refinement**
- ✅ Unit tests
- ✅ Integration tests
- ✅ Bug fixes

---

## 💡 Code Snippets

### 1. Book Entity (Copy-Paste Ready)

```csharp
// LibraryManagement.Core/Entities/Book.cs
namespace LibraryManagement.Core.Entities
{
    public class Book
    {
        public int Id { get; set; }
        public string ISBN { get; set; } = string.Empty;
        public string Title { get; set; } = string.Empty;
        public string Author { get; set; } = string.Empty;
        public string Publisher { get; set; } = string.Empty;
        public int PublicationYear { get; set; }
        public string Category { get; set; } = string.Empty;
        public int TotalCopies { get; set; }
        public int AvailableCopies { get; set; }
        public decimal Price { get; set; }
        public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
        public DateTime UpdatedAt { get; set; } = DateTime.UtcNow;
    }
}
```

### 2. Member Entity (Copy-Paste Ready)

```csharp
// LibraryManagement.Core/Entities/Member.cs
namespace LibraryManagement.Core.Entities
{
    public class Member
    {
        public int Id { get; set; }
        public string MemberId { get; set; } = string.Empty;
        public string FirstName { get; set; } = string.Empty;
        public string LastName { get; set; } = string.Empty;
        public string Email { get; set; } = string.Empty;
        public string Phone { get; set; } = string.Empty;
        public string Address { get; set; } = string.Empty;
        public DateTime MembershipDate { get; set; } = DateTime.UtcNow;
        public DateTime? ExpiryDate { get; set; }
        public bool IsActive { get; set; } = true;
        public DateTime CreatedAt { get; set; } = DateTime.UtcNow;
        public DateTime UpdatedAt { get; set; } = DateTime.UtcNow;
    }
}
```

### 3. Transaction Entity (Copy-Paste Ready)

```csharp
// LibraryManagement.Core/Entities/Transaction.cs
namespace LibraryManagement.Core.Entities
{
    public class Transaction
    {
        public int Id { get; set; }
        public int BookId { get; set; }
        public int MemberId { get; set; }
        public DateTime IssueDate { get; set; } = DateTime.UtcNow;
        public DateTime DueDate { get; set; }
        public DateTime? ReturnDate { get; set; }
        public TransactionStatus Status { get; set; }
        public decimal? FineAmount { get; set; }
        public bool FinePaid { get; set; }
        public string Notes { get; set; } = string.Empty;
        
        public Book? Book { get; set; }
        public Member? Member { get; set; }
    }

    public enum TransactionStatus
    {
        Issued,
        Returned,
        Overdue,
        Lost
    }
}
```

### 4. Simple Books Controller (Copy-Paste Ready)

```csharp
// LibraryManagement.API/Controllers/BooksController.cs
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using LibraryManagement.Infrastructure.Data;
using LibraryManagement.Core.Entities;

namespace LibraryManagement.API.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class BooksController : ControllerBase
    {
        private readonly LibraryDbContext _context;

        public BooksController(LibraryDbContext context)
        {
            _context = context;
        }

        [HttpGet]
        public async Task<ActionResult<IEnumerable<Book>>> GetBooks()
        {
            return await _context.Books.ToListAsync();
        }

        [HttpGet("{id}")]
        public async Task<ActionResult<Book>> GetBook(int id)
        {
            var book = await _context.Books.FindAsync(id);
            if (book == null)
                return NotFound();
            return book;
        }

        [HttpPost]
        public async Task<ActionResult<Book>> CreateBook(Book book)
        {
            _context.Books.Add(book);
            await _context.SaveChangesAsync();
            return CreatedAtAction(nameof(GetBook), new { id = book.Id }, book);
        }

        [HttpPut("{id}")]
        public async Task<IActionResult> UpdateBook(int id, Book book)
        {
            if (id != book.Id)
                return BadRequest();

            _context.Entry(book).State = EntityState.Modified;
            await _context.SaveChangesAsync();
            return NoContent();
        }

        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteBook(int id)
        {
            var book = await _context.Books.FindAsync(id);
            if (book == null)
                return NotFound();

            _context.Books.Remove(book);
            await _context.SaveChangesAsync();
            return NoContent();
        }
    }
}
```

---

## 🧪 Testing with Swagger

### 1. Add a Book
```json
POST /api/books
{
  "isbn": "978-0-123456-78-9",
  "title": "The Great Book",
  "author": "John Doe",
  "publisher": "ABC Publishers",
  "publicationYear": 2023,
  "category": "Fiction",
  "totalCopies": 10,
  "availableCopies": 10,
  "price": 29.99
}
```

### 2. Get All Books
```
GET /api/books
```

### 3. Search Books by Title
```
GET /api/books/search?query=Great
```

---

## 📊 Database Quick Setup

### For SQL Server Express (Free):

1. **Download & Install:**
   - https://www.microsoft.com/sql-server/sql-server-downloads
   - Choose "Express" edition

2. **Connection String:**
   ```json
   "Server=localhost\\SQLEXPRESS;Database=LibraryManagement;Trusted_Connection=true;TrustServerCertificate=true;"
   ```

### For SQLite (Easiest):

1. **Connection String:**
   ```json
   "Data Source=library.db"
   ```

2. **Change in Program.cs:**
   ```csharp
   // Use SQLite instead of SQL Server
   builder.Services.AddDbContext<LibraryDbContext>(options =>
       options.UseSqlite(builder.Configuration.GetConnectionString("DefaultConnection")));
   ```

3. **Install Package:**
   ```bash
   dotnet add package Microsoft.EntityFrameworkCore.Sqlite
   ```

---

## ⚡ Common Commands

```bash
# Build project
dotnet build

# Run project (auto-reload on changes)
dotnet watch run

# Create migration
dotnet ef migrations add MigrationName

# Update database
dotnet ef database update

# Run tests
dotnet test

# Clean build artifacts
dotnet clean

# Restore packages
dotnet restore
```

---

## 🎓 Learning Resources

### For Beginners:
1. **C# Basics:** https://docs.microsoft.com/dotnet/csharp/tour-of-csharp/
2. **ASP.NET Core Tutorial:** https://docs.microsoft.com/aspnet/core/tutorials/first-web-api
3. **Entity Framework Core:** https://docs.microsoft.com/ef/core/get-started

### Video Tutorials:
1. Microsoft Learn: https://learn.microsoft.com/training/
2. YouTube: "ASP.NET Core Web API Tutorial"
3. Pluralsight/Udemy: ASP.NET Core courses

---

## 🐛 Common Issues & Fixes

### Issue: "Database already exists"
```bash
dotnet ef database drop
dotnet ef database update
```

### Issue: "Migration failed"
```bash
dotnet ef migrations remove
dotnet ef migrations add InitialCreate
dotnet ef database update
```

### Issue: "Port already in use"
Edit `Properties/launchSettings.json` and change port numbers.

### Issue: "Package not found"
```bash
dotnet restore
dotnet clean
dotnet build
```

---

## 📱 Postman Collection

Import this JSON to test the API:

```json
{
  "info": {
    "name": "Library Management API",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Get All Books",
      "request": {
        "method": "GET",
        "header": [],
        "url": {
          "raw": "https://localhost:7xxx/api/books",
          "protocol": "https",
          "host": ["localhost"],
          "port": "7xxx",
          "path": ["api", "books"]
        }
      }
    }
  ]
}
```

---

## ✅ Final Checklist

Before deploying to production:

- [ ] All CRUD operations working
- [ ] Business rules implemented
- [ ] Error handling added
- [ ] Logging configured
- [ ] Unit tests passing
- [ ] API documented in Swagger
- [ ] Database backed up
- [ ] Connection strings secured
- [ ] CORS configured properly
- [ ] HTTPS enabled

---

## 🚀 Deployment Options

### Option 1: IIS (Windows Server)
1. Publish the app: `dotnet publish -c Release`
2. Copy to IIS folder
3. Configure IIS application pool
4. Set connection string in appsettings.json

### Option 2: Docker
```dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:7.0
WORKDIR /app
COPY ./publish .
ENTRYPOINT ["dotnet", "LibraryManagement.API.dll"]
```

### Option 3: Azure App Service
1. Right-click project → Publish
2. Choose Azure
3. Select App Service
4. Configure and deploy

---

## 🎉 Next Steps After MVP

1. **Add Authentication:**
   - JWT authentication
   - Role-based authorization (Admin, Librarian)

2. **Build Frontend:**
   - Blazor WebAssembly
   - React/Angular
   - Mobile app (MAUI)

3. **Advanced Features:**
   - Email notifications
   - SMS alerts
   - Reports and analytics
   - Barcode scanning

4. **Performance:**
   - Add caching (Redis)
   - Optimize queries
   - Add pagination

---

**Need Help?** 
- Check LIBRARY_MANAGEMENT_MVP_PLAN.md for detailed specs
- Check SETUP_INSTRUCTIONS.md for comprehensive setup guide

**Happy Building! 🎯**
