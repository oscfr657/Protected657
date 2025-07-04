
describe('template spec', () => {
  it('Logedin can upload', () => {
    cy.adminLogin(Cypress.env('username'), Cypress.env('password'))
    cy.visit(Cypress.env('baseUrl') + '/protected/');
    cy.get('h2').contains('Protected files');
    cy.get('[href="/protected/add/"]').click();
    cy.get('h1').contains('Add File');
    cy.get('#id_title').type('Cypress test');
    cy.get('#id_file').selectFile('door_logo43.png');
    cy.get('button').click();
    cy.get('tbody > :nth-child(1) > :nth-child(1)').contains('Cypress test');
  });
  it('Logedin can delete', () => {
    cy.adminLogin(Cypress.env('username'), Cypress.env('password'))
    cy.visit(Cypress.env('baseUrl') + '/admin/protected657/protectedfile/');
    cy.get('#result_list > tbody:nth-child(2) > tr:nth-child(1) > th:nth-child(2) > a:nth-child(1)').click();
    cy.get('.deletelink').click();
    cy.get('#deleted-objects > li').contains('Protected file: Cypress test');
    cy.get('div > [type="submit"]').click();
    cy.get('.success').contains('protected file “Cypress test”');
  });
  it('Logedout can\'t upload', () => {
    cy.adminLogin(Cypress.env('username'), Cypress.env('password'));
    cy.visit(Cypress.env('baseUrl') + '/admin');
    cy.get('#logout-form > button').click();
    cy.visit(Cypress.env('baseUrl') + '/protected');
    cy.get('#site-name > a').contains('Django administration');
  });
});
