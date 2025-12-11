# Library Management System - MVP Plan (C#)

## Project Overview
A comprehensive Library Management System built with C# and .NET Core that enables librarians to manage books, members, and borrowing transactions efficiently.

## Technology Stack
- **Backend Framework**: ASP.NET Core 6.0/7.0
- **Database**: SQL Server (Production) / SQLite (Development)
- **ORM**: Entity Framework Core
- **API Documentation**: Swagger/OpenAPI
- **Testing**: xUnit, Moq
- **Logging**: Serilog or NLog
- **Architecture**: Clean Architecture / Onion Architecture

---

## MVP Features

### 1. Book Management
**Priority: Must Have**

#### Features:
- Add new books to the library catalog
- Update book information (title, author, publisher, ISBN, category)
- Delete books from the catalog
- View all books
- Search books by:
  - Title
  - Author
  - ISBN
  - Category
- Track available vs. issued copies

#### Endpoints:
- `POST /api/books` - Add a new book
- `GET /api/books` - Get all books (with pagination)
- `GET /api/books/{id}` - Get book by ID
- `GET /api/books/search?query={searchTerm}` - Search books
- `PUT /api/books/{id}` - Update book details
- `DELETE /api/books/{id}` - Delete a book

#### Data Model:
```csharp
public class Book
{
    public int Id { get; set; }
    public string ISBN { get; set; }
    public string Title { get; set; }
    public string Author { get; set; }
    public string Publisher { get; set; }
    public int PublicationYear { get; set; }
    public string Category { get; set; }
    public int TotalCopies { get; set; }
    public int AvailableCopies { get; set; }
    public decimal Price { get; set; }
    public DateTime CreatedAt { get; set; }
    public DateTime UpdatedAt { get; set; }
}
```

---

### 2. Member Management
**Priority: Must Have**

#### Features:
- Register new library members
- Update member information
- Delete/Deactivate members
- View all members
- Search members by name, email, or member ID
- Track membership status (active/inactive)

#### Endpoints:
- `POST /api/members` - Register a new member
- `GET /api/members` - Get all members (with pagination)
- `GET /api/members/{id}` - Get member by ID
- `GET /api/members/search?query={searchTerm}` - Search members
- `PUT /api/members/{id}` - Update member details
- `DELETE /api/members/{id}` - Deactivate a member

#### Data Model:
```csharp
public class Member
{
    public int Id { get; set; }
    public string MemberId { get; set; } // Library card number
    public string FirstName { get; set; }
    public string LastName { get; set; }
    public string Email { get; set; }
    public string Phone { get; set; }
    public string Address { get; set; }
    public DateTime MembershipDate { get; set; }
    public DateTime? ExpiryDate { get; set; }
    public bool IsActive { get; set; }
    public DateTime CreatedAt { get; set; }
    public DateTime UpdatedAt { get; set; }
}
```

---

### 3. Transaction Management
**Priority: Must Have**

#### Features:
- Issue books to members
- Return books from members
- View all transactions
- View member's borrowing history
- Track due dates
- Validate business rules:
  - Member must be active
  - Book must be available
  - Member cannot exceed borrowing limit (e.g., 5 books)
  - Cannot issue book if member has overdue books

#### Endpoints:
- `POST /api/transactions/issue` - Issue a book
- `POST /api/transactions/return` - Return a book
- `GET /api/transactions` - Get all transactions
- `GET /api/transactions/member/{memberId}` - Get member's transaction history
- `GET /api/transactions/overdue` - Get all overdue transactions

#### Data Model:
```csharp
public class Transaction
{
    public int Id { get; set; }
    public int BookId { get; set; }
    public int MemberId { get; set; }
    public DateTime IssueDate { get; set; }
    public DateTime DueDate { get; set; }
    public DateTime? ReturnDate { get; set; }
    public TransactionStatus Status { get; set; } // Issued, Returned, Overdue
    public decimal? FineAmount { get; set; }
    public bool FinePaid { get; set; }
    public string Notes { get; set; }
    
    // Navigation properties
    public Book Book { get; set; }
    public Member Member { get; set; }
}

public enum TransactionStatus
{
    Issued,
    Returned,
    Overdue,
    Lost
}
```

---

### 4. Fine Calculation (Should Have)
**Priority: Should Have**

#### Features:
- Automatic fine calculation for overdue books
- Configure fine rate per day
- Track fine payment status
- View outstanding fines

#### Business Rules:
- Fine Rate: $1 per day (configurable)
- Maximum Fine: $50 per book (configurable)
- Grace Period: 1 day (configurable)

---

## Project Structure

```
LibraryManagement/
│
├── LibraryManagement.API/              # ASP.NET Core Web API
│   ├── Controllers/
│   │   ├── BooksController.cs
│   │   ├── MembersController.cs
│   │   └── TransactionsController.cs
│   ├── Program.cs
│   └── appsettings.json
│
├── LibraryManagement.Core/             # Domain Layer
│   ├── Entities/
│   │   ├── Book.cs
│   │   ├── Member.cs
│   │   └── Transaction.cs
│   ├── Interfaces/
│   │   ├── IBookRepository.cs
│   │   ├── IMemberRepository.cs
│   │   ├── ITransactionRepository.cs
│   │   └── IUnitOfWork.cs
│   └── Exceptions/
│       └── LibraryException.cs
│
├── LibraryManagement.Application/      # Business Logic Layer
│   ├── Services/
│   │   ├── BookService.cs
│   │   ├── MemberService.cs
│   │   └── TransactionService.cs
│   ├── DTOs/
│   │   ├── BookDto.cs
│   │   ├── MemberDto.cs
│   │   └── TransactionDto.cs
│   └── Validators/
│       ├── BookValidator.cs
│       ├── MemberValidator.cs
│       └── TransactionValidator.cs
│
├── LibraryManagement.Infrastructure/   # Data Access Layer
│   ├── Data/
│   │   └── LibraryDbContext.cs
│   ├── Repositories/
│   │   ├── BookRepository.cs
│   │   ├── MemberRepository.cs
│   │   ├── TransactionRepository.cs
│   │   └── UnitOfWork.cs
│   └── Migrations/
│
└── LibraryManagement.Tests/            # Unit & Integration Tests
    ├── UnitTests/
    │   ├── BookServiceTests.cs
    │   ├── MemberServiceTests.cs
    │   └── TransactionServiceTests.cs
    └── IntegrationTests/
        └── ApiTests.cs
```

---

## Development Phases

### Phase 1: Setup (Week 1)
- [x] Initialize .NET solution
- [ ] Create project structure (API, Core, Application, Infrastructure, Tests)
- [ ] Configure Entity Framework Core
- [ ] Set up database connection
- [ ] Configure Swagger for API documentation
- [ ] Set up logging framework

### Phase 2: Core Models (Week 1-2)
- [ ] Create domain entities (Book, Member, Transaction)
- [ ] Define repository interfaces
- [ ] Implement DbContext and configure entity relationships
- [ ] Create initial database migrations

### Phase 3: Data Access Layer (Week 2)
- [ ] Implement Repository pattern for all entities
- [ ] Implement Unit of Work pattern
- [ ] Add database seeding for test data
- [ ] Write repository unit tests

### Phase 4: Business Logic (Week 3)
- [ ] Implement Book Service with CRUD operations
- [ ] Implement Member Service with CRUD operations
- [ ] Implement Transaction Service (issue/return logic)
- [ ] Add validation logic and business rules
- [ ] Write service unit tests

### Phase 5: API Layer (Week 3-4)
- [ ] Create API controllers for Books
- [ ] Create API controllers for Members
- [ ] Create API controllers for Transactions
- [ ] Implement error handling middleware
- [ ] Add API versioning
- [ ] Configure CORS

### Phase 6: Testing & Refinement (Week 4)
- [ ] Write integration tests for API endpoints
- [ ] Perform manual testing
- [ ] Fix bugs and issues
- [ ] Optimize database queries
- [ ] Add logging for critical operations

### Phase 7: Documentation & Deployment (Week 5)
- [ ] Complete API documentation with Swagger
- [ ] Write README with setup instructions
- [ ] Create database setup scripts
- [ ] Prepare deployment configuration
- [ ] (Optional) Create Docker containerization

---

## API Endpoints Summary

### Books
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/books | Get all books |
| GET | /api/books/{id} | Get book by ID |
| GET | /api/books/search | Search books |
| POST | /api/books | Add new book |
| PUT | /api/books/{id} | Update book |
| DELETE | /api/books/{id} | Delete book |

### Members
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/members | Get all members |
| GET | /api/members/{id} | Get member by ID |
| GET | /api/members/search | Search members |
| POST | /api/members | Register member |
| PUT | /api/members/{id} | Update member |
| DELETE | /api/members/{id} | Deactivate member |

### Transactions
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/transactions | Get all transactions |
| GET | /api/transactions/member/{id} | Get member history |
| GET | /api/transactions/overdue | Get overdue books |
| POST | /api/transactions/issue | Issue a book |
| POST | /api/transactions/return | Return a book |

---

## Business Rules

### Book Issue Rules:
1. Member must be active
2. Member must not exceed borrowing limit (default: 5 books)
3. Member must not have overdue books
4. Book must have available copies
5. Default loan period: 14 days

### Book Return Rules:
1. Calculate fine if overdue
2. Update book availability
3. Update transaction status
4. Mark fine as paid/unpaid

### Member Registration Rules:
1. Email must be unique
2. Phone number must be valid
3. All required fields must be provided
4. Membership validity: 1 year from registration

---

## Database Schema

```sql
-- Books Table
CREATE TABLE Books (
    Id INT PRIMARY KEY IDENTITY(1,1),
    ISBN VARCHAR(20) UNIQUE NOT NULL,
    Title VARCHAR(200) NOT NULL,
    Author VARCHAR(200) NOT NULL,
    Publisher VARCHAR(200),
    PublicationYear INT,
    Category VARCHAR(100),
    TotalCopies INT NOT NULL,
    AvailableCopies INT NOT NULL,
    Price DECIMAL(10,2),
    CreatedAt DATETIME DEFAULT GETDATE(),
    UpdatedAt DATETIME DEFAULT GETDATE()
);

-- Members Table
CREATE TABLE Members (
    Id INT PRIMARY KEY IDENTITY(1,1),
    MemberId VARCHAR(20) UNIQUE NOT NULL,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(150) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(500),
    MembershipDate DATETIME NOT NULL,
    ExpiryDate DATETIME,
    IsActive BIT DEFAULT 1,
    CreatedAt DATETIME DEFAULT GETDATE(),
    UpdatedAt DATETIME DEFAULT GETDATE()
);

-- Transactions Table
CREATE TABLE Transactions (
    Id INT PRIMARY KEY IDENTITY(1,1),
    BookId INT FOREIGN KEY REFERENCES Books(Id),
    MemberId INT FOREIGN KEY REFERENCES Members(Id),
    IssueDate DATETIME NOT NULL,
    DueDate DATETIME NOT NULL,
    ReturnDate DATETIME,
    Status VARCHAR(20) NOT NULL,
    FineAmount DECIMAL(10,2),
    FinePaid BIT DEFAULT 0,
    Notes VARCHAR(500)
);
```

---

## Configuration Settings

```json
{
  "ConnectionStrings": {
    "DefaultConnection": "Server=.;Database=LibraryManagement;Trusted_Connection=true;"
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
      "Microsoft.AspNetCore": "Warning"
    }
  }
}
```

---

## Testing Strategy

### Unit Tests:
- Test all service methods
- Mock repository dependencies
- Test business rule validation
- Test exception handling

### Integration Tests:
- Test API endpoints with test database
- Test database operations
- Test end-to-end workflows

### Test Coverage Goal:
- Minimum 80% code coverage
- 100% coverage for business logic

---

## Deployment Considerations

### Prerequisites:
- .NET 6.0/7.0 SDK
- SQL Server 2019+ or SQLite
- IIS or Docker for hosting

### Deployment Steps:
1. Publish the application
2. Configure database connection string
3. Run database migrations
4. Configure IIS/Docker
5. Test API endpoints
6. Monitor logs

---

## Future Enhancements (Post-MVP)

1. **Authentication & Authorization**
   - Admin and Librarian roles
   - Member self-service portal
   - JWT authentication

2. **Advanced Features**
   - Book reservation system
   - Email notifications for due dates
   - Reports and analytics
   - Barcode scanning
   - Multi-branch support

3. **Frontend**
   - Web UI (Blazor/React/Angular)
   - Mobile app
   - Admin dashboard

4. **Integration**
   - Payment gateway for fines
   - SMS notifications
   - External library catalogs

---

## Timeline Estimate

**Total Duration: 4-5 weeks**

- Week 1: Setup, Models, Database
- Week 2: Data Access Layer, Repositories
- Week 3: Business Logic, Services
- Week 4: API Development, Testing
- Week 5: Documentation, Refinement, Deployment

---

## Success Criteria

The MVP is considered successful when:
- ✅ All CRUD operations work for Books, Members, and Transactions
- ✅ Books can be issued and returned with proper validation
- ✅ Overdue tracking and fine calculation works
- ✅ API documentation is complete and accurate
- ✅ Unit tests pass with >80% coverage
- ✅ Application can be deployed and runs without errors
- ✅ Basic error handling and logging is implemented

---

## Resources Needed

### Development Tools:
- Visual Studio 2022 or VS Code
- SQL Server Management Studio
- Postman or Swagger UI for API testing
- Git for version control

### Skills Required:
- C# and .NET Core
- Entity Framework Core
- ASP.NET Core Web API
- SQL Server
- Unit testing (xUnit)
- RESTful API design

---

## Risk Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| Database performance issues | High | Use indexing, optimize queries, implement caching |
| Scope creep | Medium | Stick to MVP features, document future enhancements |
| Testing gaps | Medium | Maintain minimum 80% code coverage |
| Deployment issues | High | Test in staging environment, prepare rollback plan |

---

## Conclusion

This MVP plan provides a solid foundation for a Library Management System. The focus is on core functionality that delivers immediate value while maintaining code quality and scalability for future enhancements.
