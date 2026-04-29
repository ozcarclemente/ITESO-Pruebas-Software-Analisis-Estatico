Feature: Search universities and their programs

  Scenario Outline: Search university on Google and verify related programs
    Given I open Google
    When I search for "<university>" on Google
    And I click the first link matching "<domain>"
    Then I should be on the "<domain>" website
    When I search for "<search_term>" on the university site
    Then the results should contain "<expected_keyword>"

    Examples:
      | university | domain    | search_term  | expected_keyword |
      | ITESO      | iteso.mx  | carreras     | carrera          |
      | UAG        | uag.mx    | ingeniería   | ingeniería       |
      | UP         | up.edu.mx | campus       | campus           |
      | UAG        | uag.mx    | posgrado     | posgrado         |
      | UP         | up.edu.mx | posgrados    | posgrado         |
      | ITESO      | iteso.mx  | posgrados    | posgrado         |
