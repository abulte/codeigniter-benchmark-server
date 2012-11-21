<?php
class News extends MY_Controller {

    public function __construct()
    {
        parent::__construct();
        $this->load->model('news_model');
    }

    public function index()
    {
        $data['news'] = $this->news_model->get_news();  
        $data['title'] = 'News archive';

        $this->data = $data;
        $this->_render('news/index');
    }

    public function view($slug)
    {
        $data['news_item'] = $this->news_model->get_news($slug);

        if (empty($data['news_item']))
        {
            show_404();
        }

        $data['title'] = $data['news_item']['title'];

        $this->data = $data;
        $this->_render('news/view');

    }

    public function create()
    {
        $this->load->helper('form');
        $this->load->library('form_validation');
        
        $data['title'] = 'Create a news item';
        
        $this->form_validation->set_rules('title', 'Title', 'required');
        $this->form_validation->set_rules('text', 'text', 'required');
        
        $this->data = $data;
        if ($this->form_validation->run() === FALSE)
        {
            $this->_render('news/create');
        }
        else
        {
            $this->news_model->set_news();
            $this->_render('news/success');
        }
    }
}