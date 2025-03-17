import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Section11Component } from './section11.component';

describe('Section11Component', () => {
  let component: Section11Component;
  let fixture: ComponentFixture<Section11Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Section11Component]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Section11Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
