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
public class Etudiant extends Contact {

    public String Cycle;
    public String Niveau;

    public String getCycle() {
        return Cycle;
    }

    public void setCycle(String Cycle) {
        this.Cycle = Cycle;
    }

    public String getNiveau() {
        return Niveau;
    }

    public void setNiveau(String Niveau) {
        this.Niveau = Niveau;
    }

    public Etudiant(String code, String nom, LocalDate dateNaiss, String address, String email, String telNumber, String Cycle, String niveau) {
        super(code, nom, dateNaiss, address, email, telNumber);
        this.Cycle = Cycle;
        this.Niveau = niveau;
    }

    public Etudiant() {

    }

    public void create(String code, String nom, LocalDate dateNaiss, String address, String email, String telNumber, String Cycle, String Niveau) throws SQLException, ExceptionPersonnalier {
        String sql = "INSERT INTO etudiant (code,nom,dateNaiss,address,email,telNumber,Cycle,Niveau) VALUES (?,?,?,?,?,?,?,?) ";
        PreparedStatement prestm = JDBC.getConnexion().prepareStatement(sql);
        prestm.setObject(1, code);
        prestm.setObject(2, nom);
        prestm.setObject(3, dateNaiss);
        prestm.setObject(4, address);
        prestm.setObject(5, email);
        prestm.setObject(6, telNumber);
        prestm.setObject(7, Cycle);
        prestm.setObject(8, Niveau);
        // prestm.execute();
        if (prestm.execute()) {
            throw new ExceptionPersonnalier("Erreur lors de l'enregistrement de l'etudiant veuillez contacter l'administrateur");
        }
    }

    public void updateCode(String code, String nom, LocalDate dateNaiss, String address, String email, String telNumber, String Cycle, String Niveau, String code1) throws SQLException {
        String updateSQL = "UPDATE etudiant SET code=?, nom=?, dateNaiss=?, address=? ,email=?, telNumber=?, Cycle=?, Niveau=? WHERE code=?";
        try {
            PreparedStatement pstmt = JDBC.getConnexion().prepareStatement(updateSQL);

            pstmt.setObject(1, code);
            pstmt.setObject(2, nom);
            pstmt.setObject(3, dateNaiss);
            pstmt.setObject(4, address);
            pstmt.setObject(5, email);
            pstmt.setObject(6, telNumber);
            pstmt.setObject(7, Cycle);
            pstmt.setObject(8, Niveau);
            pstmt.setObject(9, code1);
            pstmt.execute();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void deleteEtudiantById(String code) throws SQLException {
        String deleteSQL = "DELETE FROM etudiant WHERE code=?";

        try (PreparedStatement pstmt = JDBC.getConnexion().prepareStatement(deleteSQL)) {

            pstmt.setString(1, code);

            int rowsAffected = pstmt.executeUpdate();
            System.out.println("Nombre de lignes supprimées : " + rowsAffected);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public Etudiant GetOne(String code) throws SQLException {
        String sql = "select *from etudiant where code=?";
        PreparedStatement preStmt = JDBC.getConnexion().prepareStatement(sql);
        preStmt.setObject(1, code);
        ResultSet rs = preStmt.executeQuery();
        while (rs.next()) {
            return new Etudiant(rs.getString(1), rs.getString(2), rs.getDate(3).toLocalDate(), rs.getString(4), rs.getString(5), rs.getString(6), rs.getString(7), rs.getString(8));
        }
        return null;
    }

    public List<Etudiant> getAllEtudiant() throws SQLException {
        List<Etudiant> listeEtudiant = new ArrayList<>();
        String selectSQL = "SELECT * FROM etudiant";
        PreparedStatement pstmt = JDBC.getConnexion().prepareStatement(selectSQL);

        ResultSet rs = pstmt.executeQuery();
        while (rs.next()) {
            listeEtudiant.add(new Etudiant(rs.getString(1), rs.getString(2), rs.getDate(3).toLocalDate(), rs.getString(4), rs.getString(5), rs.getString(6), rs.getString(7), rs.getString(8)));
        }
        return listeEtudiant;
    }

    public static void main(String[] args) throws SQLException, ExceptionPersonnalier {
        try {
            Etudiant etudiant = new Etudiant();
            // etudiant.create("225092463", "stephane", LocalDate.of(2015, 05, 20), "ESSOS", "Bozzerstephane@gmail.com", "670585489", "Licence", 3);
            //etudiant.deleteEtudiantById("225092472");     
            //etudiant.getAllEtudiant();       
            etudiant.updateCode("265092472", "ERICA", LocalDate.of(2015, 05, 20), "ESSOS", "zikemstephane@gmail.com", "675176531", "Licence", "4", "12312s");
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
