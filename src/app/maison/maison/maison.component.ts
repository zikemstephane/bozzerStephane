import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-maison',
  imports: [CommonModule],
  templateUrl: './maison.component.html',
  styleUrl: './maison.component.css'
})
export class MaisonComponent {
   maisonse = [
    {Quartier:"Quartier Soleil", adresse: "12 rue Victor Hugo", superficie: 120, categorie: "résidentiel" },
    {Quartier:"La Forêt", adresse: "45 avenue des Champs", superficie: 300, categorie: "commercial" },
    {Quartier:"Centre-Ville", adresse: "78 boulevard Haussmann", superficie: 500, categorie: "industriel" },
    {Quartier:"Belle Vue", adresse: "3 impasse des Lilas", superficie: 95, categorie: "résidentiel" },
    {Quartier:"Le Plateau", adresse: "88 zone industrielle Nord", superficie: 750, categorie: "industriel" },
    {Quartier:"Belle Vue", adresse: "26 rue du Commerce", superficie: 200, categorie: "commercial" },
    {Quartier:"La Forêt", adresse: "14 chemin de la Forêt", superficie: 130, categorie: "résidentiel" },
    {Quartier:"Le Plateau", adresse: "59 parc d’activités Est", superficie: 600, categorie: "industriel" },
    {Quartier:"Quartier Soleil", adresse: "10 rue de la Paix", superficie: 220, categorie: "commercial" },
    {Quartier:"Centre-Ville", adresse: "7 allée des Marronniers", superficie: 105, categorie: "résidentiel" }
  ];
  
}
