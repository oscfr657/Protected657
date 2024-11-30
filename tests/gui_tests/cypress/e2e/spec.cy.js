
describe('template spec', () => {
  it('Logedin can upload', () => {
    cy.visit(Cypress.env('baseUrl') + '/admin')
    cy.get('#id_username').type(Cypress.env('username'))
    cy.get('#id_password').type(Cypress.env('password'))
    cy.get('.submit-row > input').click()
    cy.visit(Cypress.env('baseUrl') + '/protected')
    cy.get('h2').contains('Protected files')
    cy.get('[href="/protected/add/"]').click()
    cy.get('h1').contains('Add File')
    cy.get('#id_title').type('Cypress test')
    cy.get('#id_file').selectFile('door_logo43.png')
    cy.get('button').click()
    cy.get('tbody > :nth-child(1) > :nth-child(1)').contains('Cypress test')
  })
  it('Logedout can\'t upload', () => {
    cy.visit(Cypress.env('baseUrl') + '/admin')
    cy.get('#id_username').type(Cypress.env('username'))
    cy.get('#id_password').type(Cypress.env('password'))
    cy.get('.submit-row > input').click()
    cy.visit(Cypress.env('baseUrl') + '/admin/')
    cy.get('#logout-form > button').click()
    cy.visit(Cypress.env('baseUrl') + '/protected')
  })
})
