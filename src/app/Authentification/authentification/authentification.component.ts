import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { QuartierComponent } from "../../quartier/quartier/quartier.component";
import { DashbordComponent } from '../../dashbord/dashbord.component';

@Component({
  selector: 'app-authentification',
  templateUrl: './authentification.component.html',
  imports: [FormsModule, QuartierComponent,DashbordComponent],
  styleUrls: ['./authentification.component.css']
})
export class AuthentificationComponent {
  constructor(private router: Router) {}
  username: string = '';
  password: string = '';
  
  users = [
    { username: 'admin', password: 'admin' },
    { username: 'stephane', password: 'stephane' },
    { username: 'licence', password: 'licence' },
    { username: 'zikem', password: 'zikem' },
    { username: 'kuete', password: 'kuete' },
  ];

  login() {
    const user = this.users.find(u => u.username === this.username && u.password === this.password);
    if (user) {
      alert('Connexion réussie !');
      this.router.navigate(['/dashboard']);
      let usernam: String = this.username;
    } else {
      alert('Échec de la connexion !');
    }
  }

}
