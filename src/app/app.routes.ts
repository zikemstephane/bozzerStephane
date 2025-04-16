import { Routes } from '@angular/router';
import { AuthentificationComponent } from './Authentification/authentification/authentification.component';
import { CategorieComponent } from './categorie/categorie/categorie.component';
import { MaisonComponent } from './maison/maison/maison.component';
import { QuartierComponent } from './quartier/quartier/quartier.component';
import { DashbordComponent } from './dashbord/dashbord.component';
import { FormQuartierComponent } from './form-quartier/form-quartier.component';
import { FormMaisonComponent } from './form-maison/form-maison.component';
import { FormCategorieComponent } from './form-categorie/form-categorie.component';

export const routes: Routes = [
    { path: '', component: AuthentificationComponent },
    { path: 'quatier', component: QuartierComponent },
    { path: 'maison', component: MaisonComponent },
    { path: 'dashboard', component: DashbordComponent },
    { path: 'FormQuartier', component: FormQuartierComponent },
    { path: 'FormMaison', component: FormMaisonComponent },
    { path: 'categorie', component: CategorieComponent },
    { path: 'FormCategorie',component:FormCategorieComponent}
];
