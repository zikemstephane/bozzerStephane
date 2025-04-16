import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-form-categorie',
  imports: [CommonModule],
  templateUrl: './form-categorie.component.html',
  styleUrl: './form-categorie.component.css'
})
export class FormCategorieComponent {
  CATEGORIES_MAISON_MOCK = [
    { id: 1, nom: 'Villa', description: 'Grande maison individuelle souvent luxueuse.' },
    { id: 2, nom: 'Appartement', description: 'Logement dans un immeuble collectif.' },
    { id: 3, nom: 'Maison de ville', description: 'Maison en zone urbaine avec plusieurs étages.' },
    { id: 4, nom: 'Studio', description: 'Petite habitation composée d’une seule pièce.' },
    { id: 5, nom: 'Maison jumelée', description: 'Deux maisons mitoyennes partageant un mur.' },
    { id: 6, nom: 'Maison traditionnelle', description: 'Maison construite avec des matériaux locaux, style classique.' },
    { id: 7, nom: 'Maison moderne', description: 'Construction récente avec architecture contemporaine.' },
    { id: 8, nom: 'Maison en bande', description: 'Maison alignée dans une rangée, souvent avec petit jardin.' },
    { id: 9, nom: 'Maison écologique', description: 'Maison construite avec des matériaux durables et économes en énergie.' },
    { id: 10, nom: 'Maison de campagne', description: 'Maison située en milieu rural, souvent spacieuse.' }
  ];
}
