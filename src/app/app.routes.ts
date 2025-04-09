import { Routes } from '@angular/router';
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

export const routes: Routes = [
        { path: '', component: Section1Component },
        { path: 'section1', component: Section1Component },
        { path: 'section2', component: Section2Component },
        { path: 'section3', component: Section3Component },
        { path: 'section4', component: Section4Component },
        { path: 'section6', component: Section6Component },
        { path: 'section7', component: Section7Component },
        { path: 'section8', component: Section8Component },
        { path: 'section9', component: Section9Component },
        { path: 'section10', component: Section10Component },
        { path: 'section11', component: Section11Component },
        { path: '**', redirectTo: '/section1' },

];
