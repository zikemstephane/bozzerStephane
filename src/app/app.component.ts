import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from './dossier/header/header.component';
import { Section1Component } from './dossier/section1/section1.component';
import { Section2Component } from './dossier/section2/section2.component';
import { Section3Component } from './dossier/section3/section3.component';
import { Section4Component } from './dossier/section4/section4.component';
import { Section6Component } from './dossier/section6/section6.component';
import { Section7Component } from './dossier/section7/section7.component';
import { Section8Component } from './dossier/section8/section8.component';
import { Section9Component } from './dossier/section9/section9.component';
import { Section10Component } from './dossier/section10/section10.component';
import { Section11Component } from './dossier/section11/section11.component';

@Component({
  selector: 'app-root',
  imports: [ HeaderComponent,Section1Component,Section2Component,Section3Component,Section4Component,Section6Component,Section7Component,Section8Component,Section9Component,Section10Component,Section11Component, RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})

export class AppComponent {
  title = 'projet-Angular'
}
