# Library Management System - Architecture & Design

## Table of Contents
1. [System Overview](#system-overview)
2. [Architecture Pattern](#architecture-pattern)
3. [Technology Stack](#technology-stack)
4. [Project Structure](#project-structure)
5. [Data Flow](#data-flow)
6. [Database Design](#database-design)
7. [Design Patterns](#design-patterns)
8. [Security Considerations](#security-considerations)
9. [Performance Optimization](#performance-optimization)
10. [Deployment Architecture](#deployment-architecture)

---

## System Overview

The Library Management System is a RESTful API built with ASP.NET Core that enables efficient management of library operations including books, members, and borrowing transactions.

### Key Features:
- **Book Management**: CRUD operations for library catalog
- **Member Management**: Member registration and management
- **Transaction Management**: Book issue/return with business rules
- **Fine Calculation**: Automated overdue fine calculation
- **Search Functionality**: Advanced search across books and members

---

## Architecture Pattern

### Clean Architecture (Onion Architecture)

The application follows the Clean Architecture pattern with clear separation of concerns:

```
┌──────────────────────────────────────────────────┐
│              API Layer (Controllers)              │
│  - HTTP Requests/Responses                       │
│  - Input Validation                              │
│  - Error Handling                                │
└──────────────────┬───────────────────────────────┘
                   │
┌──────────────────▼───────────────────────────────┐
│         Application Layer (Services)              │
│  - Business Logic                                │
│  - DTOs & Mapping                                │
│  - Validation Rules                              │
└──────────────────┬───────────────────────────────┘
                   │
┌──────────────────▼───────────────────────────────┐
│            Core Layer (Domain)                    │
│  - Entities                                      │
│  - Interfaces                                    │
│  - Business Rules                                │
└──────────────────▲───────────────────────────────┘
                   │
┌──────────────────┴───────────────────────────────┐
│      Infrastructure Layer (Data Access)           │
│  - EF Core DbContext                             │
│  - Repositories                                  │
│  - Database Migrations                           │
└──────────────────────────────────────────────────┘
```

### Dependency Rule:
- **Core** has no dependencies
- **Application** depends only on Core
- **Infrastructure** depends only on Core
- **API** depends on Application and Infrastructure

---

## Technology Stack

### Backend Framework:
- **ASP.NET Core 6.0/7.0**: Web API framework
- **C# 10/11**: Programming language
- **.NET SDK**: Runtime and tooling

### Data Access:
- **Entity Framework Core 7.x**: ORM
- **SQL Server**: Primary database (Production)
- **SQLite**: Alternative database (Development)
- **LINQ**: Query language

### API Documentation:
- **Swagger/OpenAPI**: API documentation and testing
- **Swashbuckle**: Swagger implementation for .NET

### Testing:
- **xUnit**: Unit testing framework
- **Moq**: Mocking framework
- **FluentAssertions**: Assertion library
- **EF Core InMemory**: Database for integration tests

### Logging:
- **Serilog**: Structured logging
- **Microsoft.Extensions.Logging**: Logging abstraction

### Validation:
- **FluentValidation**: Input validation
- **Data Annotations**: Model validation

### Mapping:
- **AutoMapper**: Object-to-object mapping

---

## Project Structure

```
LibraryManagement/
│
├── LibraryManagement.API/
│   ├── Controllers/
│   │   ├── BooksController.cs
│   │   ├── MembersController.cs
│   │   └── TransactionsController.cs
│   ├── Middleware/
│   │   ├── ErrorHandlingMiddleware.cs
│   │   └── LoggingMiddleware.cs
│   ├── Filters/
│   │   └── ValidationFilter.cs
│   ├── Program.cs
│   ├── appsettings.json
│   └── appsettings.Development.json
│
├── LibraryManagement.Core/
│   ├── Entities/
│   │   ├── Book.cs
│   │   ├── Member.cs
│   │   └── Transaction.cs
│   ├── Interfaces/
│   │   ├── Repositories/
│   │   │   ├── IBookRepository.cs
│   │   │   ├── IMemberRepository.cs
│   │   │   ├── ITransactionRepository.cs
│   │   │   └── IUnitOfWork.cs
│   │   └── Services/
│   │       ├── IBookService.cs
│   │       ├── IMemberService.cs
│   │       └── ITransactionService.cs
│   ├── Enums/
│   │   └── TransactionStatus.cs
│   └── Exceptions/
│       ├── LibraryException.cs
│       ├── BookNotAvailableException.cs
│       └── MemberInactiveException.cs
│
├── LibraryManagement.Application/
│   ├── Services/
│   │   ├── BookService.cs
│   │   ├── MemberService.cs
│   │   └── TransactionService.cs
│   ├── DTOs/
│   │   ├── BookDto.cs
│   │   ├── CreateBookDto.cs
│   │   ├── UpdateBookDto.cs
│   │   ├── MemberDto.cs
│   │   ├── TransactionDto.cs
│   │   └── IssueBookDto.cs
│   ├── Validators/
│   │   ├── BookValidator.cs
│   │   ├── MemberValidator.cs
│   │   └── TransactionValidator.cs
│   ├── Mappings/
│   │   └── MappingProfile.cs
│   └── Common/
│       ├── Result.cs
│       └── PagedResult.cs
│
├── LibraryManagement.Infrastructure/
│   ├── Data/
│   │   ├── LibraryDbContext.cs
│   │   └── DbInitializer.cs
│   ├── Repositories/
│   │   ├── BaseRepository.cs
│   │   ├── BookRepository.cs
│   │   ├── MemberRepository.cs
│   │   ├── TransactionRepository.cs
│   │   └── UnitOfWork.cs
│   ├── Configurations/
│   │   ├── BookConfiguration.cs
│   │   ├── MemberConfiguration.cs
│   │   └── TransactionConfiguration.cs
│   └── Migrations/
│       └── (auto-generated migrations)
│
└── LibraryManagement.Tests/
    ├── UnitTests/
    │   ├── Services/
    │   │   ├── BookServiceTests.cs
    │   │   ├── MemberServiceTests.cs
    │   │   └── TransactionServiceTests.cs
    │   └── Validators/
    │       └── BookValidatorTests.cs
    ├── IntegrationTests/
    │   ├── Controllers/
    │   │   └── BooksControllerTests.cs
    │   └── Repositories/
    │       └── BookRepositoryTests.cs
    └── TestHelpers/
        ├── TestDbContext.cs
        └── TestDataFactory.cs
```

---

## Data Flow

### Request Flow (Example: Create Book)

```
1. HTTP POST Request
   ↓
2. BooksController.CreateBook()
   ↓
3. Input Validation (Data Annotations + FluentValidation)
   ↓
4. BookService.CreateBookAsync(CreateBookDto)
   ↓
5. Business Logic Validation
   ↓
6. AutoMapper: DTO → Entity
   ↓
7. BookRepository.AddAsync(Book)
   ↓
8. UnitOfWork.SaveChangesAsync()
   ↓
9. Entity Framework Core
   ↓
10. SQL Server Database
   ↓
11. Response (Book Entity)
   ↓
12. AutoMapper: Entity → DTO
   ↓
13. HTTP 201 Created Response
```

### Book Issue Flow

```
1. POST /api/transactions/issue
   ↓
2. TransactionController.IssueBook()
   ↓
3. TransactionService.IssueBookAsync()
   ↓
4. Validation Checks:
   - Member is active?
   - Member not exceeded limit?
   - No overdue books?
   - Book available?
   ↓
5. Create Transaction Entity
   ↓
6. Update Book.AvailableCopies (-1)
   ↓
7. Save Transaction + Update Book (in transaction)
   ↓
8. Return Success Response
```

---

## Database Design

### Entity Relationship Diagram

```
┌─────────────────┐
│      Book       │
├─────────────────┤
│ Id (PK)         │
│ ISBN (UK)       │
│ Title           │
│ Author          │
│ Publisher       │
│ PublicationYear │
│ Category        │
│ TotalCopies     │
│ AvailableCopies │
│ Price           │
│ CreatedAt       │
│ UpdatedAt       │
└────────┬────────┘
         │
         │ 1:N
         │
┌────────▼────────────┐
│    Transaction      │
├─────────────────────┤
│ Id (PK)             │
│ BookId (FK)         │◄────┐
│ MemberId (FK)       │     │
│ IssueDate           │     │
│ DueDate             │     │
│ ReturnDate          │     │
│ Status              │     │
│ FineAmount          │     │
│ FinePaid            │     │
│ Notes               │     │
└─────────────────────┘     │
                            │ N:1
                            │
                   ┌────────┴────────┐
                   │     Member      │
                   ├─────────────────┤
                   │ Id (PK)         │
                   │ MemberId (UK)   │
                   │ FirstName       │
                   │ LastName        │
                   │ Email (UK)      │
                   │ Phone           │
                   │ Address         │
                   │ MembershipDate  │
                   │ ExpiryDate      │
                   │ IsActive        │
                   │ CreatedAt       │
                   │ UpdatedAt       │
                   └─────────────────┘
```

### Indexes

**Books Table:**
- Primary Key: `Id`
- Unique Index: `ISBN`
- Index: `Title`, `Author`, `Category` (for search)

**Members Table:**
- Primary Key: `Id`
- Unique Index: `Email`, `MemberId`
- Index: `FirstName`, `LastName` (for search)

**Transactions Table:**
- Primary Key: `Id`
- Foreign Key: `BookId`, `MemberId`
- Index: `Status`, `DueDate` (for overdue queries)
- Composite Index: `(MemberId, Status)` (for member history)

---

## Design Patterns

### 1. Repository Pattern
**Purpose:** Abstract data access logic

```csharp
public interface IBookRepository
{
    Task<Book> GetByIdAsync(int id);
    Task<IEnumerable<Book>> GetAllAsync();
    Task<Book> AddAsync(Book book);
    Task UpdateAsync(Book book);
    Task DeleteAsync(int id);
    Task<IEnumerable<Book>> SearchAsync(string query);
}
```

### 2. Unit of Work Pattern
**Purpose:** Manage transactions across multiple repositories

```csharp
public interface IUnitOfWork : IDisposable
{
    IBookRepository Books { get; }
    IMemberRepository Members { get; }
    ITransactionRepository Transactions { get; }
    Task<int> SaveChangesAsync();
}
```

### 3. Service Layer Pattern
**Purpose:** Encapsulate business logic

```csharp
public interface IBookService
{
    Task<BookDto> GetBookByIdAsync(int id);
    Task<BookDto> CreateBookAsync(CreateBookDto dto);
    Task<bool> IsBookAvailableAsync(int bookId);
}
```

### 4. DTO Pattern
**Purpose:** Data transfer between layers

```csharp
public class BookDto
{
    public int Id { get; set; }
    public string Title { get; set; }
    public string Author { get; set; }
    public int AvailableCopies { get; set; }
}
```

### 5. Result Pattern
**Purpose:** Standardized operation results

```csharp
public class Result<T>
{
    public bool Success { get; set; }
    public T Data { get; set; }
    public string ErrorMessage { get; set; }
    public List<string> Errors { get; set; }
}
```

### 6. Strategy Pattern (Future)
**Purpose:** Different fine calculation strategies

```csharp
public interface IFineCalculationStrategy
{
    decimal CalculateFine(int daysOverdue);
}
```

---

## Security Considerations

### MVP (Current):
- ✅ Input validation (prevent SQL injection)
- ✅ HTTPS enforcement
- ✅ CORS configuration
- ✅ Error handling (no sensitive data in errors)

### Post-MVP:
- [ ] Authentication (JWT)
- [ ] Authorization (role-based)
- [ ] Rate limiting
- [ ] API key validation
- [ ] Audit logging
- [ ] Data encryption at rest
- [ ] Secure password storage

### Best Practices:
1. **Never expose sensitive data** in API responses
2. **Validate all inputs** on both client and server
3. **Use parameterized queries** (EF Core handles this)
4. **Implement HTTPS** for all communications
5. **Log security events** (failed auth, suspicious activity)

---

## Performance Optimization

### Database Optimization:
1. **Indexing**: Proper indexes on frequently queried columns
2. **Pagination**: Always paginate large result sets
3. **Query Optimization**: Use `.AsNoTracking()` for read-only queries
4. **Connection Pooling**: Built-in with EF Core
5. **Async Operations**: Use async/await throughout

### Code Optimization:
```csharp
// Good: Async + No Tracking
public async Task<IEnumerable<Book>> GetBooksAsync()
{
    return await _context.Books
        .AsNoTracking()
        .ToListAsync();
}

// Good: Pagination
public async Task<PagedResult<Book>> GetBooksAsync(int page, int pageSize)
{
    var query = _context.Books.AsNoTracking();
    var totalCount = await query.CountAsync();
    
    var books = await query
        .Skip((page - 1) * pageSize)
        .Take(pageSize)
        .ToListAsync();
    
    return new PagedResult<Book>(books, totalCount, page, pageSize);
}

// Good: Selective Loading
public async Task<Book> GetBookWithTransactionsAsync(int id)
{
    return await _context.Books
        .Include(b => b.Transactions)
        .FirstOrDefaultAsync(b => b.Id == id);
}
```

### Caching Strategy (Future):
- **In-Memory Cache**: For frequently accessed data (book categories, etc.)
- **Distributed Cache**: Redis for scalability
- **Cache Invalidation**: Clear cache on data updates

---

## Deployment Architecture

### Development Environment:
```
Developer Machine
├── Visual Studio/VS Code
├── SQL Server LocalDB / SQLite
├── .NET SDK 7.0
└── Git
```

### Production Environment (Basic):
```
┌─────────────────────────────────┐
│         Load Balancer            │
└────────────┬────────────────────┘
             │
    ┌────────┴────────┐
    │                 │
┌───▼────┐      ┌────▼───┐
│ API    │      │ API    │
│ Server │      │ Server │
│ (IIS)  │      │ (IIS)  │
└───┬────┘      └────┬───┘
    │                │
    └────────┬───────┘
             │
      ┌──────▼───────┐
      │  SQL Server  │
      │   Database   │
      └──────────────┘
```

### Cloud Deployment (Azure):
```
┌─────────────────────────────────┐
│    Azure Application Gateway     │
└────────────┬────────────────────┘
             │
      ┌──────▼───────┐
      │  Azure App   │
      │   Service    │
      │  (Web API)   │
      └──────┬───────┘
             │
      ┌──────▼───────────┐
      │  Azure SQL       │
      │  Database        │
      └──────────────────┘
             │
      ┌──────▼───────────┐
      │ Application      │
      │ Insights         │
      │ (Monitoring)     │
      └──────────────────┘
```

### Docker Deployment:
```dockerfile
# Dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:7.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
WORKDIR /src
COPY ["LibraryManagement.API/LibraryManagement.API.csproj", "LibraryManagement.API/"]
RUN dotnet restore "LibraryManagement.API/LibraryManagement.API.csproj"
COPY . .
WORKDIR "/src/LibraryManagement.API"
RUN dotnet build "LibraryManagement.API.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "LibraryManagement.API.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "LibraryManagement.API.dll"]
```

---

## Monitoring & Logging

### Logging Levels:
- **Trace**: Detailed debugging information
- **Debug**: Development-time information
- **Information**: General application flow
- **Warning**: Abnormal events that don't stop the application
- **Error**: Errors and exceptions
- **Critical**: Critical failures requiring immediate attention

### What to Log:
```csharp
// Information
_logger.LogInformation("Book {BookId} issued to member {MemberId}", bookId, memberId);

// Warning
_logger.LogWarning("Member {MemberId} attempting to borrow with overdue books", memberId);

// Error
_logger.LogError(ex, "Failed to create book with ISBN {ISBN}", book.ISBN);
```

### Metrics to Track:
- Request count per endpoint
- Response times
- Error rates
- Database query performance
- Active users
- Books issued/returned per day

---

## Scalability Considerations

### Horizontal Scaling:
- Stateless API design (no session state in API)
- Database connection pooling
- Load balancer ready

### Vertical Scaling:
- Optimize queries
- Add indexes
- Increase server resources

### Future Enhancements:
- **Microservices**: Split into separate services (Books, Members, Transactions)
- **CQRS**: Separate read and write operations
- **Event Sourcing**: Track all state changes as events
- **Message Queue**: Async processing (email notifications, reports)

---

## Testing Strategy

### Unit Tests (80% Coverage Goal):
```csharp
[Fact]
public async Task CreateBook_ValidInput_ReturnsBook()
{
    // Arrange
    var mockRepo = new Mock<IBookRepository>();
    var service = new BookService(mockRepo.Object);
    var dto = new CreateBookDto { Title = "Test", ... };
    
    // Act
    var result = await service.CreateBookAsync(dto);
    
    // Assert
    result.Should().NotBeNull();
    result.Title.Should().Be("Test");
}
```

### Integration Tests:
```csharp
[Fact]
public async Task GetBooks_ReturnsOk()
{
    // Arrange
    var factory = new WebApplicationFactory<Program>();
    var client = factory.CreateClient();
    
    // Act
    var response = await client.GetAsync("/api/books");
    
    // Assert
    response.StatusCode.Should().Be(HttpStatusCode.OK);
}
```

---

## Configuration Management

### appsettings.json Structure:
```json
{
  "ConnectionStrings": {
    "DefaultConnection": "..."
  },
  "LibrarySettings": {
    "MaxBooksPerMember": 5,
    "LoanPeriodDays": 14,
    "FinePerDay": 1.00
  },
  "Serilog": {
    "MinimumLevel": "Information"
  }
}
```

### Environment-Specific:
- `appsettings.Development.json`: Development settings
- `appsettings.Production.json`: Production settings
- Environment variables: Secrets and connection strings

---

## Conclusion

This architecture provides:
- ✅ **Maintainability**: Clear separation of concerns
- ✅ **Testability**: Dependency injection, interfaces
- ✅ **Scalability**: Stateless design, async operations
- ✅ **Security**: Input validation, HTTPS
- ✅ **Performance**: Optimized queries, caching strategy
- ✅ **Extensibility**: Easy to add new features

The Clean Architecture approach ensures the system can evolve and scale as requirements grow beyond the MVP.
