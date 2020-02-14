Feature: black jack

  Scenario: repartir mano
    Given una baraja
      When reparto la carta
      Then obtengo mano
