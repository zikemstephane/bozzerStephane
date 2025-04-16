import { Component,OnInit } from '@angular/core';

@Component({
  selector: 'app-dashbord',
  imports: [],
  templateUrl: './dashbord.component.html',
  styleUrl: './dashbord.component.css'
})
export class DashbordComponent implements OnInit{
  gestionnaire = {
    nom: 'Mamadou Traoré',
    email: 'mamadou@gmail.com'
  };

  quartiers = [
    { nom: 'Quartier Soleil', superficie: 1500, nbMaisons: 25 },
    { nom: 'Quartier Nord', superficie: 1200, nbMaisons: 18 },
    { nom: 'Quartier Est', superficie: 1700, nbMaisons: 30 }
  ];
  ngOnInit(): void { }
  getTotalMaisons(): number {
    return this.quartiers.reduce((total, q) => total + q.nbMaisons, 0);
  }
}
