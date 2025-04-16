import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor() { }
  private _username: string = '';

  setUsername(username: string) {
    this._username = username;
  }

  getUsername(): string {
    return this._username;
  }

  isLoggedIn(): boolean {
    return this._username !== '';
  }
}
