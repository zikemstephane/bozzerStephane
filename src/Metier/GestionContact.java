/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Metier;

import NewException.ExceptionPersonnalier;
import entities.Agent;
import entities.Enseignant;
import entities.Etudiant;
import java.sql.SQLException;
import java.time.LocalDate;
import java.util.List;

/**
 *
 * @author User
 */
public class GestionContact {
       // private Versement verse;

    public void creerEtudiant(Etudiant e) throws SQLException, ExceptionPersonnalier {
        Etudiant e1 = new Etudiant();
        e1.create(e.getCode(), e.getNom(), e.getDateNaiss(), e.getAddress(), e.getEmail(), e.getTelNumber(), e.getCycle(), e.getNiveau());
    }
    public void creerEnseignant(Enseignant e) throws SQLException, ExceptionPersonnalier {
        Enseignant e1 = new Enseignant();
        e1.create(e.getCode(), e.getNom(), e.getDateNaiss(), e.getAddress(), e.getEmail(), e.getTelNumber(), e.getStatut());
    }
    public void creerAgent(Agent e) throws SQLException, ExceptionPersonnalier {
        Agent e1 = new Agent();
//String code, String nom, LocalDate dateNaiss, String address, String email, String telNumber,String statut, int Salaire,  String Categorie, int Indicesalaire, String occupation
        e1.createAgent(e.getCode(), e.getNom(), e.getDateNaiss(), e.getAddress(), e.getEmail(), e.getTelNumber(),e.getSalaire(),e.getStatut(),e1.getCategorie(),e.getIndicesalaire(),e.getOccupation());
    }
//"265092472", "ERICA", LocalDate.of(2015, 05, 20), "ESSOS", "zikemstephane@gmail.com", "675176531", "Licence", "4","12312s"
    public void modifierEtudiant(Etudiant e) throws SQLException, ExceptionPersonnalier {
        Etudiant e1 = new Etudiant();
        e1.updateCode(e.getCode(), e.getNom(), e.getDateNaiss(), e.getAddress(), e.getEmail(), e.getTelNumber(), e.getCycle(), e.getNiveau(),e.getCode());
    }
    public void modifierEnseignant(Enseignant e) throws SQLException, ExceptionPersonnalier {
        Enseignant e1 = new Enseignant();
        e1.updateEmail(e.getCode(), e.getNom(), e.getDateNaiss(), e.getAddress(), e.getEmail(), e.getTelNumber(),e.getStatut(),e.getCode());
    }
    public void modifierAgent(Agent e) throws SQLException, ExceptionPersonnalier {
        Agent e1 = new Agent();
//String code, String nom, LocalDate dateNaiss, String address, String email, String telNumber, String Salaire,String statut,  String Categorie, String Indicesalaire, String occupation
       // e1.updateAgent(e.getCode(),e.getNom(), e.getDateNaiss(),e.getAddress(),e.getEmail(),e.getTelNumber(),e.getSalaire(),e.getStatut(),e.getCategorie(),e.getIndicesalaire(),e.getOccupation(),e.getCode());
    }
    //public void creerVersement(Versement e) throws SQLException, ExceptionPersonnalier {
      //  Versement v = new Versement();
        //v.create(e.getMatricule(), e.getDate(), e.getMontant());
    //}

    public List<Etudiant> listerEtudiant() throws SQLException{
        Etudiant e = new Etudiant();
        return e.getAllEtudiant();
    }
    public List<Enseignant> listerEnseignant() throws SQLException{
        Enseignant e = new Enseignant();
        return e.getAllEnseignant();
    }
    public List<Agent> listerAgent() throws SQLException{
        Agent e = new Agent();
        return e.getAllAgent();
    }
}

