# Black Box Tests

## Equivalence Partitioning

### 1. Function that validates credit card numbers.

- Valid card numbers: Length between 13 and 16 digits, containing only numeric digits.

| Test Case | Description                    | Input             | Expected Result |
| --------- | ------------------------------ | ----------------- | --------------- |
| TC1       | Length < 13 (numeric)          | 123456789012      | Not valid       |
| TC2       | Length between 13–16 (numeric) | 12345678901234    | Valid           |
| TC3       | Length > 16 (numeric)          | 12345678901234567 | Not valid       |
| TC4       | Non-numeric input              | 1234567890123A    | Not valid       |
| TC5       | Empty input                    | ""                | Not valid       |

### 2. Function that validates dates.

- Valid years: Between 1900 and 2100.
- Valid months: Between 1 and 12.
- Valid days: Between 1 and 31.

| Test Case | Description      | Year | Month | Day | Expected Result |
| --------- | ---------------- | ---- | ----- | --- | --------------- |
| TC1       | All valid values | 1999 | 6     | 15  | Valid           |
| TC2       | Year < 1900      | 1899 | 6     | 15  | Not valid       |
| TC3       | Year > 2100      | 2101 | 6     | 15  | Not valid       |
| TC4       | Month < 1        | 1999 | 0     | 15  | Not valid       |
| TC5       | Month > 12       | 1999 | 13    | 15  | Not valid       |
| TC6       | Day < 1          | 1999 | 6     | 0   | Not valid       |
| TC7       | Day > 31         | 1999 | 6     | 32  | Not valid       |

### 3. Function that checks the eligibility of a passenger to book a flight.

- Eligible ages: Between 18 and 65.
- Frequent flyers: True or False.

| Test Case | Description            | Age | Frequent Flyer | Expected Result |
| --------- | ---------------------- | --- | -------------- | --------------- |
| TC1       | Valid age (FF = True)  | 30  | True           | Eligible        |
| TC2       | Age < 18               | 17  | False          | Not eligible    |
| TC3       | Age > 65               | 75  | True           | Not eligible    |
| TC4       | Valid age (FF = False) | 30  | False          | Eligible        |

### 4. Function that validates URLs.

- Valid URLs: Length less than or equal to 255, starting with "http://" or "https://"

| Test Case | Description                   | URL                      | Expected Result |
| --------- | ----------------------------- | ------------------------ | --------------- |
| TC1       | Valid prefix and valid length | http://example.com       | Valid           |
| TC2       | Length > 255                  | http:// + 256 characters | Not valid       |
| TC3       | Invalid prefix                | ftp://example.com        | Not valid       |

# Boundary Value Analysis

### 1. Function that calculates the eligibility of a person for a loan based on their income and credit score.

The eligibility rules are as follows:

- If the income is less than $30,000, the person is not eligible for a loan.
- If the income is between $30,000 and $60,000 (inclusive) and the credit score is above 700, the person is eligible for a standard loan.
- If the income is between $30,000 and $60,000 (inclusive) and the credit score is below or equal to 700, the person is eligible for a secured loan.
- If the income is greater than $60,000 and the credit score is above 750, the person is eligible for a premium loan.
- If the income is greater than $60,000 and the credit score is between 700 and 750 (inclusive), the person is eligible for a standard loan.

| Test Case | Description                            | Income | Credit Score | Expected Result |
| --------- | -------------------------------------- | ------ | ------------ | --------------- |
| TC1       | Just below 30k                         | 29,999 | 720          | Not eligible    |
| TC2       | At 30k, score >700                     | 30,000 | 701          | Standard loan   |
| TC3       | At 30k, score =700                     | 30,000 | 700          | Secured loan    |
| TC4       | At 30k, score <700                     | 30,000 | 699          | Secured loan    |
| TC5       | Just below 60k                         | 59,999 | 700          | Secured loan    |
| TC6       | At 60k, score >700                     | 60,000 | 701          | Standard loan   |
| TC7       | Above 60k, score <700 (undefined case) | 60,001 | 699          | Not specified   |
| TC8       | Above 60k, score =700                  | 60,001 | 700          | Standard loan   |
| TC9       | Boundary at 750                        | 60,001 | 750          | Standard loan   |
| TC10      | Above 750                              | 60,001 | 751          | Premium loan    |

### 2. Function that determines the category of a product in an e-commerce system based on its price.

The product categories and pricing rules are as follows:

- Category A: Products priced between $10 and $50 (inclusive).
- Category B: Products priced between $51 and $100 (inclusive).
- Category C: Products priced between $101 and $200 (inclusive).
- Category D: Products priced above $200.

| Test Case | Description                          | Price | Expected Result          |
| --------- | ------------------------------------ | ----- | ------------------------ |
| TC1       | price < 10                           | 9     | Not valid / Out of range |
| TC2       | price = 10 (Category A lower bound)  | 10    | Category A               |
| TC3       | price > 10 (Category A)              | 11    | Category A               |
| TC4       | price < 50 (Category A)              | 49    | Category A               |
| TC5       | price = 50 (Category A upper bound)  | 50    | Category A               |
| TC6       | price = 51 (Category B lower bound)  | 51    | Category B               |
| TC7       | price > 51 (Category B)              | 52    | Category B               |
| TC8       | price < 100 (Category B)             | 99    | Category B               |
| TC9       | price = 100 (Category B upper bound) | 100   | Category B               |
| TC10      | price = 101 (Category C lower bound) | 101   | Category C               |
| TC11      | price > 101 (Category C)             | 102   | Category C               |
| TC12      | price < 200 (Category C)             | 199   | Category C               |
| TC13      | price = 200 (Category C upper bound) | 200   | Category C               |
| TC14      | price > 200 (Category D)             | 201   | Category D               |

### 3. Function that calculates the cost of shipping for packages based on their weight and dimensions.

The shipping cost rules are as follows:

- If the weight of the package is less than or equal to 1 kg and the dimensions (length, width, and height) are each less than or equal to 10 cm, the cost is $5.
- If the weight is between 1 and 5 kg (inclusive) and the dimensions are each between 11 and 30 cm (inclusive), the cost is $10.
- If the weight is greater than 5 kg or any of the dimensions is greater than 30 cm, the cost is $20.

| Test Case | Description                                    | Weight (kg) | Length (cm) | Width (cm) | Height (cm) | Expected Result |
| --------- | ---------------------------------------------- | ----------- | ----------- | ---------- | ----------- | --------------- |
| TC1       | Just below 1kg and dimensions <10              | 0.99        | 9.9         | 9.9        | 9.9         | 5               |
| TC2       | Boundary dimensions =10 with weight <1         | 0.99        | 10          | 10         | 10          | 5               |
| TC3       | Boundary weight =1 with dimensions <10         | 1.00        | 9.9         | 9.9        | 9.9         | 5               |
| TC4       | Boundary weight =1 and dimensions =10          | 1.00        | 10          | 10         | 10          | 5               |
| TC5       | Just above 1kg and dimensions =11              | 1.10        | 11          | 11         | 11          | 10              |
| TC6       | Just above 1kg and dimensions =30              | 1.10        | 30          | 30         | 30          | 10              |
| TC7       | Boundary weight =5 and dimensions =11          | 5.00        | 11          | 11         | 11          | 10              |
| TC8       | Boundary weight =5 and dimensions =30          | 5.00        | 30          | 30         | 30          | 10              |
| TC9       | Just above 5kg                                 | 5.10        | 30          | 30         | 30          | 20              |
| TC10      | One dimension >30                              | 2.00        | 30.1        | 30         | 30          | 20              |
| TC11      | Undefined case (1<weight≤5 and dimensions ≤10) | 2.00        | 10          | 10         | 10          | Not specified   |

# Decision Table

### 1. Create the decision table for a system that provides weather advisories based on temperature and humidity.

The rules are:

- Weather recommendation "High temperature and humidity. Stay hydrated." for temperature > 30 and humidity > 70.
- Weather recommendation "Low temperature. Don't forget your jacket!" for temperature < 0 and any humidity.
- No weather recommendation for any other temperature and humidity combination.

| Rule | Temperature   | Humidity | Output                                        |
| ---- | ------------- | -------- | --------------------------------------------- |
| R1   | > 30          | > 70     | High temperature and humidity. Stay hydrated. |
| R2   | > 30          | ≤ 70     | No recommendation                             |
| R3   | < 0           | Any      | Low temperature. Don't forget your jacket!    |
| R4   | 0 ≤ temp ≤ 30 | Any      | No recommendation                             |

### 2. Create the decision table for a system that authenticates users based on their username and password.

The rules are:

- Returns "Admin" for username "admin" and password "admin123".
- Returns "User" for any other username with at least 5 characters and password with at least 8 characters.
- Returns "Invalid" if the username or password lengths are not met.

| Rule | Username                     | Password       | Output  |
| ---- | ---------------------------- | -------------- | ------- |
| R1   | "admin"                      | "admin123"     | Admin   |
| R2   | ≠ "admin" and ≥ 5 characters | ≥ 8 characters | User    |
| R3   | < 5 characters               | Any            | Invalid |
| R4   | ≥ 5 characters               | < 8 characters | Invalid |
| R5   | "admin"                      | ≠ "admin123"   | Invalid |
