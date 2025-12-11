# Library Management System - FAQ & Glossary

## Frequently Asked Questions (FAQ)

### General Questions

#### Q1: What is the purpose of this Library Management System?
**A:** This system is designed to help libraries manage their operations efficiently, including:
- Maintaining a catalog of books
- Managing library members
- Tracking book borrowing and returns
- Calculating fines for overdue books
- Searching for books and member information

#### Q2: Why C# and ASP.NET Core?
**A:** C# and ASP.NET Core offer:
- High performance and scalability
- Strong typing and compile-time error checking
- Rich ecosystem of libraries and tools
- Cross-platform support (Windows, Linux, macOS)
- Excellent documentation and community support
- Built-in dependency injection and middleware
- Easy integration with modern databases

#### Q3: Is this suitable for production use?
**A:** The MVP is designed to demonstrate core functionality and can be used for:
- Small to medium-sized libraries
- Learning and educational purposes
- Proof of concept for larger systems

For production use in large libraries, consider adding:
- Authentication and authorization
- Enhanced security measures
- Performance optimization
- Backup and disaster recovery
- Advanced reporting features

#### Q4: Can I use this for a school/college library?
**A:** Absolutely! The system is well-suited for educational institutions. You may want to add:
- Student ID integration
- Class/department categorization
- Semester-based membership
- Integration with student information systems

#### Q5: What database should I use?
**A:** 
- **Development**: SQLite (simple, no setup required)
- **Small Libraries**: SQL Server Express (free, up to 10GB)
- **Large Libraries**: SQL Server Standard/Enterprise or Azure SQL
- **Alternative**: PostgreSQL, MySQL (requires adapter changes)

---

### Technical Questions

#### Q6: Do I need Visual Studio?
**A:** No, you have options:
- **Visual Studio 2022** (Windows/Mac) - Full IDE with GUI tools
- **VS Code** (All platforms) - Lightweight with extensions
- **JetBrains Rider** (All platforms) - Premium IDE
- **Command Line** - Just .NET SDK and text editor

#### Q7: What version of .NET should I use?
**A:** 
- **Recommended**: .NET 7.0 (latest stable with long-term support)
- **Minimum**: .NET 6.0 (LTS version, supported until Nov 2024)
- **Future**: .NET 8.0+ (when available)

#### Q8: How do I handle database migrations in production?
**A:**
1. **Never** run migrations directly in production
2. Generate SQL scripts: `dotnet ef migrations script`
3. Review and test scripts in staging
4. Have DBA execute scripts in production
5. Keep migration history synchronized

#### Q9: Can I add authentication later?
**A:** Yes! The architecture supports adding JWT authentication:
```csharp
// Add to Program.cs
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(options => { /* config */ });

// Add [Authorize] attribute to controllers
[Authorize(Roles = "Librarian")]
public class BooksController : ControllerBase
```

#### Q10: How do I deploy to Azure?
**A:**
1. Right-click project → Publish
2. Choose Azure → Azure App Service
3. Create new or select existing App Service
4. Configure connection strings in Azure Portal
5. Deploy!

See: https://docs.microsoft.com/azure/app-service/quickstart-dotnetcore

#### Q11: Can I use this with React/Angular frontend?
**A:** Yes! The API is designed to be consumed by any frontend:
- React SPA
- Angular application
- Vue.js app
- Blazor WebAssembly
- Mobile apps (React Native, Flutter, MAUI)

Just configure CORS properly in Program.cs.

#### Q12: How do I enable HTTPS in development?
**A:**
```bash
dotnet dev-certs https --trust
```
This creates and trusts a development certificate.

---

### Business Logic Questions

#### Q13: Can I change the borrowing limit?
**A:** Yes, modify in `appsettings.json`:
```json
"LibrarySettings": {
  "MaxBooksPerMember": 10  // Change from 5 to 10
}
```

#### Q14: How are fines calculated?
**A:** 
```
Fine = (Return Date - Due Date) × Fine Per Day

Example:
- Due Date: Jan 15
- Return Date: Jan 20
- Days Overdue: 5
- Fine Per Day: $1.00
- Total Fine: $5.00
```

Maximum fine is capped at $50 per book (configurable).

#### Q15: What happens if a member loses a book?
**A:** In MVP:
1. Mark transaction status as "Lost"
2. Charge replacement cost
3. Remove from member's borrowed count

Future enhancement: Add book replacement workflow.

#### Q16: Can members reserve books?
**A:** Not in MVP. Future enhancement:
- Add Reservation entity
- Queue system for popular books
- Notification when book becomes available

#### Q17: How do I handle book renewals?
**A:** Future enhancement. Implementation would:
1. Check if book is reserved by another member
2. Check if member hasn't exceeded renewal limit
3. Extend due date by loan period
4. Update transaction record

---

### Data Questions

#### Q18: How do I seed initial data?
**A:** Create a `DbInitializer` class:
```csharp
public static class DbInitializer
{
    public static void Seed(LibraryDbContext context)
    {
        if (context.Books.Any()) return; // Already seeded
        
        context.Books.AddRange(
            new Book { Title = "Book 1", ... },
            new Book { Title = "Book 2", ... }
        );
        context.SaveChanges();
    }
}
```

Call in Program.cs after app.Build().

#### Q19: How do I backup the database?
**A:**
**SQL Server:**
```sql
BACKUP DATABASE LibraryManagement
TO DISK = 'C:\Backups\LibraryManagement.bak'
```

**SQLite:**
Simply copy the .db file.

#### Q20: Can I import books from CSV/Excel?
**A:** Future enhancement. Would require:
1. File upload endpoint
2. CSV/Excel parsing library
3. Validation of imported data
4. Bulk insert operation

---

### Testing Questions

#### Q21: How do I run tests?
**A:**
```bash
# All tests
dotnet test

# Specific test
dotnet test --filter "FullyQualifiedName~BookServiceTests"

# With coverage
dotnet test /p:CollectCoverage=true
```

#### Q22: Do I need a separate test database?
**A:** For integration tests:
- Use EF Core InMemory database (fastest)
- Or use separate test SQL Server/SQLite database
- Never use production database for testing!

#### Q23: How do I test with Postman?
**A:**
1. Import the Postman collection (see QUICK_START_GUIDE.md)
2. Set base URL variable
3. Run requests in sequence:
   - Create book
   - Create member
   - Issue book
   - Return book

---

### Performance Questions

#### Q24: How many concurrent users can it handle?
**A:** Depends on:
- Server resources (CPU, RAM)
- Database performance
- Network bandwidth
- Query optimization

Typical ASP.NET Core API can handle:
- Small server: 100-500 concurrent users
- Medium server: 500-2000 concurrent users
- Large server: 2000+ concurrent users

#### Q25: How do I improve performance?
**A:**
1. **Add caching** for frequently accessed data
2. **Optimize queries** - use AsNoTracking() for reads
3. **Add indexes** on frequently queried columns
4. **Enable response compression**
5. **Use pagination** for large datasets
6. **Consider Redis** for distributed caching

#### Q26: Should I use stored procedures?
**A:** Generally not needed for CRUD operations. Consider for:
- Complex business logic
- Reporting queries
- Batch operations
- Performance-critical operations

---

## Glossary

### General Terms

**API (Application Programming Interface)**
- A set of endpoints that allow external applications to interact with the system.

**REST (Representational State Transfer)**
- An architectural style for building web services using HTTP methods (GET, POST, PUT, DELETE).

**Endpoint**
- A specific URL path that performs a particular operation (e.g., `/api/books`).

**CRUD**
- Create, Read, Update, Delete - the four basic operations for data management.

**MVP (Minimum Viable Product)**
- A version with just enough features to satisfy early customers and provide feedback.

---

### C# / .NET Terms

**ASP.NET Core**
- Microsoft's framework for building web applications and APIs.

**.NET SDK**
- Software Development Kit containing tools to build .NET applications.

**NuGet**
- Package manager for .NET, similar to npm for JavaScript.

**Entity Framework Core (EF Core)**
- Object-Relational Mapper (ORM) that enables .NET developers to work with databases using objects.

**LINQ (Language Integrated Query)**
- Query syntax built into C# for querying collections and databases.

**Middleware**
- Software components that handle requests and responses in the HTTP pipeline.

**Dependency Injection (DI)**
- Design pattern for providing objects with their dependencies.

**Controller**
- Class that handles HTTP requests and returns HTTP responses.

**Action Method**
- Method in a controller that responds to HTTP requests.

**Model Binding**
- Process of mapping HTTP request data to action method parameters.

**Data Annotations**
- Attributes used to define validation rules and database mappings.

---

### Database Terms

**Migration**
- Code that updates the database schema to match the model changes.

**DbContext**
- Gateway to the database; represents a session with the database.

**DbSet**
- Collection of entities that can be queried from the database.

**Entity**
- A class that maps to a database table.

**Primary Key (PK)**
- Unique identifier for a database record.

**Foreign Key (FK)**
- Field that links to the primary key of another table.

**Index**
- Database structure that improves query performance.

**Seeding**
- Populating the database with initial/test data.

**Connection String**
- Configuration string containing database connection details.

**ORM (Object-Relational Mapping)**
- Technique for converting data between incompatible systems (objects ↔ relational database).

---

### Architecture Terms

**Clean Architecture**
- Software design pattern that separates concerns into layers.

**Repository Pattern**
- Pattern that encapsulates data access logic.

**Unit of Work**
- Pattern that maintains a list of objects affected by a transaction.

**DTO (Data Transfer Object)**
- Object that carries data between layers/processes.

**Service Layer**
- Layer containing business logic.

**Domain Model**
- Objects representing business entities and rules.

**Separation of Concerns**
- Design principle for separating a program into distinct sections.

---

### HTTP Terms

**HTTP Methods:**
- **GET**: Retrieve data
- **POST**: Create new data
- **PUT**: Update existing data
- **DELETE**: Remove data
- **PATCH**: Partial update

**Status Codes:**
- **200 OK**: Success
- **201 Created**: Resource created successfully
- **204 No Content**: Success with no response body
- **400 Bad Request**: Invalid input
- **404 Not Found**: Resource not found
- **500 Internal Server Error**: Server error

**CORS (Cross-Origin Resource Sharing)**
- Security feature that controls which domains can access the API.

---

### Testing Terms

**Unit Test**
- Test that verifies a single unit of code (method/function) in isolation.

**Integration Test**
- Test that verifies multiple components working together.

**Mock**
- Fake object that simulates real object behavior for testing.

**Assertion**
- Statement that checks if a condition is true in a test.

**Code Coverage**
- Percentage of code executed during tests.

**Test Fixture**
- Fixed state used as baseline for running tests.

---

### Library-Specific Terms

**Catalog**
- Complete list of all books in the library.

**ISBN (International Standard Book Number)**
- Unique identifier for books.

**Circulation**
- Process of lending and returning books.

**Due Date**
- Date by which a borrowed book must be returned.

**Overdue**
- Book not returned by the due date.

**Fine**
- Penalty charged for returning a book late.

**Patron**
- Another term for library member.

**Acquisition**
- Process of adding new books to the library.

**Loan Period**
- Duration for which a book can be borrowed (default: 14 days).

**Hold/Reservation**
- Request to borrow a book that's currently unavailable.

---

## Troubleshooting Index

Quick links to common issues:

- **Build Errors**: See SETUP_INSTRUCTIONS.md → Troubleshooting
- **Migration Issues**: See SETUP_INSTRUCTIONS.md → EF Core Commands
- **Database Connection**: See SETUP_INSTRUCTIONS.md → Database Connection Failed
- **Port Conflicts**: See QUICK_START_GUIDE.md → Common Issues
- **HTTPS Certificate**: Run `dotnet dev-certs https --trust`
- **Package Restore**: Run `dotnet restore`

---

## Resources

### Official Documentation
- **.NET**: https://docs.microsoft.com/dotnet
- **ASP.NET Core**: https://docs.microsoft.com/aspnet/core
- **Entity Framework Core**: https://docs.microsoft.com/ef/core
- **C# Guide**: https://docs.microsoft.com/dotnet/csharp

### Learning Resources
- **Microsoft Learn**: https://learn.microsoft.com
- **Pluralsight**: ASP.NET Core courses
- **YouTube**: .NET Channel, Tim Corey
- **Books**: "C# in Depth", "ASP.NET Core in Action"

### Community
- **Stack Overflow**: https://stackoverflow.com/questions/tagged/asp.net-core
- **Reddit**: r/dotnet, r/csharp
- **Discord**: .NET Discord Community
- **GitHub**: https://github.com/dotnet

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-01-15 | Initial MVP plan and documentation |

---

**Need more help?** 
- Check the other documentation files
- Search Stack Overflow
- Ask in the .NET community forums
- Create an issue in the repository

**Happy Coding! 🎉**
