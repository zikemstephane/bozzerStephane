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
import javax.swing.JOptionPane;

/**
 *
 * @author User
 */
public class Enseignant extends Contact {

    public String Statut;

    public Enseignant(String code, String nom, LocalDate dateNaiss, String address, String email, String telNumber, String Statut) {
        super(code, nom, dateNaiss, address, email, telNumber);
        this.Statut = Statut;
    }

    public String getStatut() {
        return Statut;
    }

    public void setStatut(String Statut) {
        this.Statut = Statut;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }

    public LocalDate getDateNaiss() {
        return dateNaiss;
    }

    public void setDateNaiss(LocalDate dateNaiss) {
        this.dateNaiss = dateNaiss;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getTelNumber() {
        return telNumber;
    }

    public void setTelNumber(String telNumber) {
        this.telNumber = telNumber;
    }

    public Enseignant() {
    }

    public void create(String code, String nom, LocalDate dateNaiss, String address, String email, String telNumber, String Statut) throws SQLException, ExceptionPersonnalier {
        String sql = "INSERT INTO enseignant (code,nom,dateNaiss,address,email,telNumber,Statut) VALUES (?,?,?,?,?,?,?) ";
        PreparedStatement prestm = JDBC.getConnexion().prepareStatement(sql);
        prestm.setObject(1, code);
        prestm.setObject(2, nom);
        prestm.setObject(3, dateNaiss);
        prestm.setObject(4, address);
        prestm.setObject(5, email);
        prestm.setObject(6, telNumber);
        prestm.setObject(7, Statut);
        // prestm.execute();
        if (prestm.execute()) {
            throw new ExceptionPersonnalier("Erreur lors de l'enregistrement de l'etudiant veuillez contacter l'administrateur");
        }
    }

    public void updateEmail(String code, String nom, LocalDate dateNaiss, String address, String email, String telNumber, String Statut, String code1) throws SQLException {
        String updateSQL = "UPDATE enseignant SET code=? nom=? dateNaiss=? address=? email=? telNumber=? Statut=? WHERE code=?";

        try (PreparedStatement pstmt = JDBC.getConnexion().prepareStatement(updateSQL)) {

            pstmt.setString(1, code);
            pstmt.setString(2, nom);
            pstmt.setObject(3, dateNaiss);
            pstmt.setString(4, address);
            pstmt.setString(5, email);
            pstmt.setString(6, telNumber);
            pstmt.setString(7, Statut);
            pstmt.setString(8, code1);
            pstmt.execute();
            int rowsAffected = pstmt.executeUpdate();
            System.out.println("Nombre de lignes affectées : " + rowsAffected);

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void deleteEtudiantById(String code) throws SQLException {
        String deleteSQL = "DELETE FROM Enseignant WHERE code=?";

        try (PreparedStatement pstmt = JDBC.getConnexion().prepareStatement(deleteSQL)) {

            pstmt.setString(1, code);

            int rowsAffected = pstmt.executeUpdate();
            System.out.println("Nombre de lignes supprimées : " + rowsAffected);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public Enseignant getOne(String code) throws SQLException {
        String sql = "select *from Enseignant where code=?";
        PreparedStatement preStmt = JDBC.getConnexion().prepareStatement(sql);
        preStmt.setObject(1, code);
        ResultSet rs = preStmt.executeQuery();
        while (rs.next()) {
            return new Enseignant(rs.getString(1), rs.getString(2), rs.getDate(3).toLocalDate(), rs.getString(4), rs.getString(5), rs.getString(6), rs.getString(7));
        }
        return null;
    }

    public List<Enseignant> getAllEnseignant() throws SQLException {
        List<Enseignant> listeEnseignant = new ArrayList<>();
        String selectSQL = "SELECT * FROM Enseignant";
        PreparedStatement pstmt = JDBC.getConnexion().prepareStatement(selectSQL);

        ResultSet rs = pstmt.executeQuery();
        while (rs.next()) {
            listeEnseignant.add(new Enseignant(rs.getString(1), rs.getString(2), rs.getDate(3).toLocalDate(), rs.getString(4), rs.getString(5), rs.getString(6), rs.getString(7)));
        }
        return listeEnseignant;
    }

    public static void main(String[] args) throws SQLException, ExceptionPersonnalier {
        try {
            Enseignant enseignant = new Enseignant();
            //enseignant.create("225092463", "stephane", LocalDate.of(2015, 05, 20), "ESSOS", "Bozzerstephane@gmail.com", "670585489", "Vacataire");
            //etudiant.deleteEtudiantById("225092472");     
            //etudiant.getAllEtudiant();       
           enseignant.updateEmail("265092472", "Ravily", LocalDate.of(2006, 8, 18), "Nkoabang", "Ravily@gmail.com", "679760291", "Vacataire", "214563");
            //etudiant.updateEmail("bozzerstephane@gmail.com", "670585489");
            //List<Etudiant> listEtudiant = etudiant.getAllEtudiant();
            //for(Etudiant e : listeEtudiant){
            //System.out.println(e.getCode());
            //}

        } catch (SQLException ex) {
            ex.printStackTrace();
        }
    }
}
