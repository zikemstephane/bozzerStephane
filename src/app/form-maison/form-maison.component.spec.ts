import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FormMaisonComponent } from './form-maison.component';

describe('FormMaisonComponent', () => {
  let component: FormMaisonComponent;
  let fixture: ComponentFixture<FormMaisonComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FormMaisonComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FormMaisonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
