import { Router } from '@angular/router';
import { routes } from './../../app.routes';
import { CommonModule } from '@angular/common';
import { Component ,Input,OnInit} from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-quartier',
  imports: [FormsModule,CommonModule],
  templateUrl: './quartier.component.html',
  styleUrl: './quartier.component.css'
})
export class QuartierComponent implements OnInit{
  constructor(private route: Router) { }
 
  nom: string = '';
  description: string = '';
  superficie: number | null = null;
  @Input() administrateur: string = '';
  usernam: string = ''
  
  ngOnInit(): string {
    return this.usernam = localStorage.getItem('usernam') || '';
  }


  

  QUARTIERS_MOCK = [
    {
      nom: "Quartier Soleil",
      superficie: 2500,
      description: "Un quartier résidentiel calme avec de beaux jardins."
    },
    {
      nom: "Belle Vue",
      superficie: 1800,
      description: "Situé en hauteur, avec une vue magnifique sur la ville."
    },
    {
      nom: "Centre-Ville",
      superficie: 3200,
      description: "Le cœur économique et commercial de la ville."
    },
    {
      nom: "Les Alizés",
      superficie: 2100,
      description: "Quartier moderne avec des immeubles récents."
    },
    {
      nom: "La Forêt",
      superficie: 4000,
      description: "Entouré de verdure, parfait pour les familles."
    },
    {
      nom: "Le Plateau",
      superficie: 2800,
      description: "Zone mixte avec habitations et petits commerces."
    },
    {
      nom: "Cité Lumière",
      superficie: 2300,
      description: "Un quartier bien éclairé avec une ambiance conviviale."
    },
    {
      nom: "Nord-Est",
      superficie: 3500,
      description: "Très dynamique avec de nombreux projets en développement."
    },
    {
      nom: "Zone Industrielle",
      superficie: 5000,
      description: "Réservée aux activités économiques et aux entrepôts."
    },
    {
      nom: "Les Jardins",
      superficie: 1900,
      description: "Connu pour ses parcs et sa tranquillité."
    }
  ];

  
}
