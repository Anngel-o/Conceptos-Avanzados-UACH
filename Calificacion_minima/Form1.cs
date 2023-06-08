using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Califa_Minima
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void calcNotas(double c1)
        {
            double c2, c3, prome = 60;

            c1 = Convert.ToDouble(txtc1.Text);
            c2 = (prome - (3 * c1)) / 7;
            c3 = (prome - (3 * c1)) / 7;

            txtc2.Text = c2.ToString();
            txtc3.Text = c3.ToString();

            if (c1 <= 0)
            {
                pnlcero.Visible = true;
            }
            if (c1 >= 10.01)
            {
                pnldiez.Visible = true;
            }
        }

        private void calcNotas(double c1, double c2)
        {
            //prom = (c1 * 0.03) + (c2 * 0.03) + (c3 * 0.04);

            //(c2 ) = (-c1 * 0.03) + 6 /  0.03
            double c3, prome = 60;

            c1 = Convert.ToDouble(txtc1.Text);
            c2 = Convert.ToDouble(txtc1.Text);
            c3 = ( prome - (3 * c1) - (3 * c2) ) / 4;
            //c3 = Convert.ToDouble(txtc3.Text);
            //c3 = double.Parse(txtc3.Text);
            txtc3.Text = c3.ToString();

            if (c1 < 0.0 || c2 < 0.0)
            {
                pnlcero.Visible = true;
            }
            if (c1 > 10.0 || c2 > 10.0)
            {
                pnldiez.Visible = true;
            }
        }

        private void calcNotas(double c1, double c2, double c3)
        {
            double prom;

            c1 = double.Parse(txtc1.Text);
            c2 = double.Parse(txtc2.Text);
            c3 = double.Parse(txtc3.Text);

            prom = (c1 * 0.03) + (c2 * 0.03) + (c3 * 0.04);

            txtprom.Text = prom.ToString();

            if (c1 < 0.0 || c2 < 0.0 || c3 < 0.0 )
            {
                pnlcero.Visible = true;
            }
            if (c1 > 10.0 || c2 > 10.0 || c3 > 10.0)
            {
                pnldiez.Visible = true;
            }
            if(prom < 6)
            {
                MessageBox.Show("El alumno no alcanza promedio mínimo", "ALUMNO REPROBADO", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            }
        }

        private void btnc1_Click(object sender, EventArgs e)
        {
            try
            {
                double c1;
                c1 = Convert.ToDouble(txtc1.Text);
                calcNotas(c1);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
        private void btnc2_Click(object sender, EventArgs e)
        {
            try
            {
                double c1, c2;
                c1 = Convert.ToDouble(txtc1.Text);
                c2 = Convert.ToDouble(txtc2.Text);
                calcNotas(c1, c2);
            }
            catch
            {
                MessageBox.Show("Sólo se permite introducir números", "ERROR", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }   
        }
        private void button3_Click(object sender, EventArgs e)
        {
            try
            {
                double c1, c2, c3;
                c1 = double.Parse(txtc1.Text);
                c2 = double.Parse(txtc2.Text);
                c3 = double.Parse(txtc3.Text);
                calcNotas(c1, c2, c3);
            }
            catch
            {
                MessageBox.Show("Sólo se permite introducir números", "ERROR", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void btnnuevo_Click(object sender, EventArgs e)
        {
            txtc1.Clear();
            txtc2.Clear();
            txtc3.Clear();
            txtprom.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            pnlcero.Visible = false;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            pnldiez.Visible = false;
            //se eliminó este botón
        }

        private void button2_Click_1(object sender, EventArgs e)
        {
            pnldiez.Visible = false;
        }

        private void btnclose_Click(object sender, EventArgs e)
        {
            Close();
        }


    }
}
