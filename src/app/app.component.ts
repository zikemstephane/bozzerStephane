import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { AuthentificationComponent } from './Authentification/authentification/authentification.component';
import { CategorieComponent } from './categorie/categorie/categorie.component';
import { MaisonComponent } from './maison/maison/maison.component';
import { QuartierComponent } from './quartier/quartier/quartier.component';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet,AuthentificationComponent,CategorieComponent,MaisonComponent,QuartierComponent,FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'Gestion_Quartier';
}
