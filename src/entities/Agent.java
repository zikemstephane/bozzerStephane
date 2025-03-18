/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package entities;

import NewException.ExceptionPersonnalier;
import Utils.JDBC;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author User
 */
public class Agent extends Contact {

    public String Salaire;
    public String Statut;
    public String Categorie;
    public String Indicesalaire;
    public String occupation;

    public Agent(String code, String nom, LocalDate dateNaiss, String address, String email, String telNumber, String Salaire, String Statut, String Categorie, String Indicesalaire, String occupation) {
        super(code, nom, dateNaiss, address, email, telNumber);
        this.Salaire = Salaire;
        this.Statut = Statut;
        this.Categorie = Categorie;
        this.Indicesalaire = Indicesalaire;
        this.occupation = occupation;
    }
public Agent(){}
    public String getSalaire() {
        return Salaire;
    }

    public void setSalaire(String Salaire) {
        this.Salaire = Salaire;
    }

    public String getStatut() {
        return Statut;
    }

    public void setStatut(String Statut) {
        this.Statut = Statut;
    }

    public String getCategorie() {
        return Categorie;
    }

    public void setCategorie(String Categorie) {
        this.Categorie = Categorie;
    }

    public String getIndicesalaire() {
        return Indicesalaire;
    }

    public void setIndicesalaire(String Indicesalaire) {
        this.Indicesalaire = Indicesalaire;
    }

    public String getOccupation() {
        return occupation;
    }

    public void setOccupation(String occupation) {
        this.occupation = occupation;
    }
    public void createAgent(String code, String nom, LocalDate dateNaissEnLocalDate, String addresse, String emaile, String telephone, String salaire,String statut,String categorie,String Indice,String Occupation) throws SQLException, ExceptionPersonnalier {
        String sql = "INSERT INTO Agent (code,nom,dateNaiss,adresse,email,telNumber,salaire,statut,categorie,Indicesalaire,occupation) VALUES (?,?,?,?,?,?,?,?,?,?,?) ";
        PreparedStatement prestm = JDBC.getConnexion().prepareStatement(sql);
        prestm.setObject(1, code);
        prestm.setObject(2, nom);
        prestm.setObject(3, dateNaissEnLocalDate);
        prestm.setObject(4, addresse);
        prestm.setObject(5, emaile);
        prestm.setObject(6, telephone);
        prestm.setObject(7, salaire);
        prestm.setObject(8, statut);
        prestm.setObject(9, categorie);
        prestm.setObject(10, Indice);
        prestm.setObject(11, Occupation);
       // prestm.execute();
        if (prestm.execute()) {
            throw new ExceptionPersonnalier("Erreur lors de l'enregistrement de l'etudiant veuillez contacter l'administrateur");
           }  
    }

    public void updateAgent(String code, String nom, LocalDate dateNaiss, String address, String email, String telNumber, String Salaire,String statut,  String Categorie, String Indicesalaire, String occupation) throws SQLException {
        String updateSQL = "UPDATE Agent SET code=? nom=? dateNaiss=? address=? email=? telNumber=? Statut=? Salaire=?,Categorie=?, Indicesalaire=?,occupation=? WHERE code=?";

        try (PreparedStatement pstmt = JDBC.getConnexion().prepareStatement(updateSQL)) {

        pstmt.setObject(1, code);
        pstmt.setObject(2, nom);
        pstmt.setObject(3, dateNaiss);
        pstmt.setObject(4, address);
        pstmt.setObject(5, email);
        pstmt.setObject(6, telNumber);
        pstmt.setObject(7, Salaire);
        pstmt.setObject(8, Categorie);
        pstmt.setObject(9, occupation);
        pstmt.setObject( 10, Indicesalaire);
        pstmt.setObject(11, statut);

            int rowsAffected = pstmt.executeUpdate();
            System.out.println("Nombre de lignes affectées : " + rowsAffected);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void deleteAgentById(String code) throws SQLException {
        String deleteSQL = "DELETE FROM Agent WHERE code=?";

        try (PreparedStatement pstmt = JDBC.getConnexion().prepareStatement(deleteSQL)) {

            pstmt.setString(1, code);

            int rowsAffected = pstmt.executeUpdate();
            System.out.println("Nombre de lignes supprimées : " + rowsAffected);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public  Agent getOneAgent(String code) throws SQLException {
        String sql = "select *from Agent where code=?";
        PreparedStatement preStmt = JDBC.getConnexion().prepareStatement(sql);
        preStmt.setObject(1, code);
        ResultSet rs = preStmt.executeQuery();
        while (rs.next()) {
            return new Agent(rs.getString(1), rs.getString(2), rs.getDate(3).toLocalDate(), rs.getString(4), rs.getString(5), rs.getString(6),rs.getString(7),rs.getString(8),rs.getString(9),rs.getString(10),rs.getString(11));
        }
        return null;
    }

    public List<Agent> getAllAgent() throws SQLException {
        List<Agent> listeAgent = new ArrayList<>();
        String selectSQL = "SELECT * FROM Agent";
        PreparedStatement pstmt = JDBC.getConnexion().prepareStatement(selectSQL);
       
        ResultSet rs = pstmt.executeQuery();
        while (rs.next()) {
            listeAgent.add(new Agent(rs.getString(1), rs.getString(2), rs.getDate(3).toLocalDate(), rs.getString(4), rs.getString(5), rs.getString(6),rs.getString(7),rs.getString(8),rs.getString(9),rs.getString(10),rs.getString(11)));
        }
        return listeAgent;
    }

}
